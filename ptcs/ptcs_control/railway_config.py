from pydantic import BaseModel, Field
from .components import Joint, Junction, Section, Train


class RailwayConfig(BaseModel):
    """
    路線の設定
    """

    # NOTE: Junction などを "" で囲むと ForwardRef に関するエラーが起こる

    junctions: dict[Junction, "JunctionConfig"] = Field(default_factory=dict)
    sections: dict[Section, "SectionConfig"] = Field(default_factory=dict)
    trains: dict[Train, "TrainConfig"] = Field(default_factory=dict)

    def define_junctions(self, *junction_tuples: tuple["Junction"]) -> None:
        """
        分岐・合流点を一斉に定義する。

        形式: `(ID,)`
        """
        for (junction_id,) in junction_tuples:
            self.junctions[junction_id] = JunctionConfig()

    def define_sections(
        self, *section_tuples: tuple["Section", "Junction", "Joint", "Junction", "Joint", float]
    ) -> None:
        """
        区間を一斉に定義する。

        形式: `(ID, j0のID, j0との接続方法, j1のID, j1との接続方法, 長さ[mm])`
        """
        for section_id, junction_0_id, junction_0_joint, junction_1_id, junction_1_joint, length in section_tuples:
            self.junctions[junction_0_id].add_section(junction_0_joint, section_id)
            self.junctions[junction_1_id].add_section(junction_1_joint, section_id)
            self.sections[section_id] = SectionConfig(
                junction_0=junction_0_id,
                junction_1=junction_1_id,
                length=length,
            )

    def define_trains(self, *train_tuples: tuple["Train"]) -> None:
        for (train_id,) in train_tuples:
            self.trains[train_id] = TrainConfig()


class JunctionConfig(BaseModel):
    sections: dict[Joint, "Section"] = Field(default_factory=dict)

    def add_section(self, joint: "Joint", section: "Section") -> None:
        self.sections[joint] = section


class SectionConfig(BaseModel):
    junction_0: "Junction"
    junction_1: "Junction"
    length: float

    def get_opposite_junction(self, junction: "Junction") -> "Junction":
        if junction == self.junction_0:
            return self.junction_1
        elif junction == self.junction_1:
            return self.junction_0
        else:
            raise


class TrainConfig(BaseModel):
    pass


RailwayConfig.update_forward_refs()


def init_config() -> RailwayConfig:
    config = RailwayConfig()

    j0a = Junction("j0a")
    j0b = Junction("j0b")
    j1a = Junction("j1a")
    j1b = Junction("j1b")

    s0 = Section("s0")
    s1 = Section("s1")
    s2 = Section("s2")
    s3 = Section("s3")
    s4 = Section("s4")
    s5 = Section("s5")

    t0 = Train("t0")
    t1 = Train("t1")

    config.define_junctions(
        (j0a,),
        (j0b,),
        (j1a,),
        (j1b,),
    )

    config.define_sections(
        (s0, j0a, Joint.CONVERGING, j0b, Joint.THROUGH, 100),
        (s1, j0b, Joint.CONVERGING, j1b, Joint.CONVERGING, 100),
        (s2, j1b, Joint.THROUGH, j1a, Joint.CONVERGING, 100),
        (s3, j1a, Joint.THROUGH, j0a, Joint.THROUGH, 100),
        (s4, j0a, Joint.DIVERGING, j0b, Joint.DIVERGING, 100),
        (s5, j1a, Joint.DIVERGING, j1b, Joint.DIVERGING, 100),
    )

    config.define_trains(
        (t0,),
        (t1,),
    )

    return config