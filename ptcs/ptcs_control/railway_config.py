import math

from pydantic import BaseModel, Field

from .components import Joint, Junction, Position, Section, Station, Stop, Train
from .constants import (
    CURVE_RAIL,
    STRAIGHT_1_4_RAIL,
    STRAIGHT_1_6_RAIL,
    STRAIGHT_RAIL,
    U_TURN_RAIL,
    WATARI_RAIL_A,
    WATARI_RAIL_B,
    WATARI_RAIL_C,
)


class RailwayConfig(BaseModel):
    """
    路線の設定
    """

    # NOTE: Junction などを "" で囲むと ForwardRef に関するエラーが起こる

    junctions: dict[Junction, "JunctionConfig"] = Field(default_factory=dict)
    sections: dict[Section, "SectionConfig"] = Field(default_factory=dict)
    trains: dict[Train, "TrainConfig"] = Field(default_factory=dict)
    stations: dict[Station, "StationConfig"] = Field(default_factory=dict)
    stops: dict[Stop, "StopConfig"] = Field(default_factory=dict)
    positions: dict[Position, "PositionConfig"] = Field(default_factory=dict)

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
        for (
            section_id,
            junction_0_id,
            junction_0_joint,
            junction_1_id,
            junction_1_joint,
            length,
        ) in section_tuples:
            self.junctions[junction_0_id].add_section(junction_0_joint, section_id)
            self.junctions[junction_1_id].add_section(junction_1_joint, section_id)
            self.sections[section_id] = SectionConfig(
                junction_0=junction_0_id,
                junction_1=junction_1_id,
                length=length,
            )

    def define_trains(self, *train_tuples: tuple["Train", int, int, float, float]) -> None:
        for (
            train_id,
            min_input,
            max_input,
            max_speed,
            delta_per_motor_rotation,
        ) in train_tuples:
            self.trains[train_id] = TrainConfig(
                min_input=min_input,
                max_input=max_input,
                max_speed=max_speed,
                delta_per_motor_rotation=delta_per_motor_rotation,
            )


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
    min_input: int
    max_input: int
    max_speed: float
    delta_per_motor_rotation: float  # モータ1回転で進む距離[cm]

    def calc_input(self, speed: float) -> int:
        if speed > self.max_speed:
            return self.max_input
        elif speed <= 0:
            return 0
        else:
            return math.floor(self.min_input + (self.max_input - self.min_input) * speed / self.max_speed)


class StationConfig(BaseModel):
    stops: list["Stop"] = Field(default_factory=list)


class StopConfig(BaseModel):
    section: "Section"
    target_junction: "Junction"
    mileage: float


class PositionConfig(BaseModel):
    section: "Section"
    mileage: float

    target_junction: "Junction"
    """
    NOTE: 将来的にはここに向きの情報を持たせなくて良いようにする。
    具体的には、通った向きがわかるようなセンシング技術を用いるか、
    計算で向きを予測するか（限界はある）のどちらか。
    """


RailwayConfig.update_forward_refs()


def init_config() -> RailwayConfig:
    config = RailwayConfig()

    j0a = Junction("j0")
    j0b = Junction("j1")
    j1a = Junction("j2")
    j1b = Junction("j3")

    s0 = Section("s0")
    s1 = Section("s1")
    s2 = Section("s2")
    s3 = Section("s3")
    s4 = Section("s4")
    s5 = Section("s5")

    t0 = Train("t0")
    t1 = Train("t1")

    station_0 = Station("station_0")
    station_1 = Station("station_1")

    stop_0 = Stop("stop_0")
    stop_1 = Stop("stop_1")
    stop_2 = Stop("stop_2")
    stop_3 = Stop("stop_3")
    stop_4 = Stop("stop_4")

    position_80 = Position("position_80")
    position_138 = Position("position_138")
    position_173 = Position("position_173")
    position_255 = Position("position_255")

    config.define_junctions(
        (j0a,),
        (j0b,),
        (j1a,),
        (j1b,),
    )

    config.define_sections(
        (
            s0,
            j0a,
            Joint.CONVERGING,
            j0b,
            Joint.THROUGH,
            WATARI_RAIL_B * 1 + STRAIGHT_RAIL * 14 + CURVE_RAIL * 8 + STRAIGHT_1_4_RAIL * 1 + WATARI_RAIL_A * 1,
        ),
        (s1, j0b, Joint.CONVERGING, j1b, Joint.CONVERGING, STRAIGHT_RAIL * 3 + WATARI_RAIL_B * 2),
        (
            s2,
            j1b,
            Joint.THROUGH,
            j1a,
            Joint.CONVERGING,
            WATARI_RAIL_A * 1 + STRAIGHT_RAIL * 6 + CURVE_RAIL * 8 + STRAIGHT_1_4_RAIL * 1 + WATARI_RAIL_B * 1,
        ),
        (s3, j1a, Joint.THROUGH, j0a, Joint.THROUGH, WATARI_RAIL_A * 2 + STRAIGHT_RAIL * 3),
        (s4, j0a, Joint.DIVERGING, j0b, Joint.DIVERGING, WATARI_RAIL_C),
        (s5, j1a, Joint.DIVERGING, j1b, Joint.DIVERGING, WATARI_RAIL_C),
    )

    config.define_trains(
        (t0, 70, 130, 40.0, 0.2435 * 0.9),  # Dr
        (t1, 90, 130, 40.0, 0.1919 * 1.1 * 0.9),  # E6
        # E5はAPS故障につきまだ運用しない
    )

    config.stations.update(
        {
            station_0: StationConfig(stops=[stop_0, stop_1]),
            station_1: StationConfig(stops=[stop_2, stop_3, stop_4]),
        }
    )

    config.stops.update(
        {
            stop_0: StopConfig(section=s0, target_junction=j0b, mileage=WATARI_RAIL_B * 1 + STRAIGHT_RAIL * 4.5),
            stop_1: StopConfig(
                section=s0,
                target_junction=j0b,
                mileage=WATARI_RAIL_B * 1 + STRAIGHT_RAIL * 10.0 + CURVE_RAIL * 8 + STRAIGHT_1_4_RAIL * 1,
            ),
            stop_2: StopConfig(section=s1, target_junction=j0b, mileage=WATARI_RAIL_B * 1 + STRAIGHT_RAIL * 1.5),
            stop_3: StopConfig(section=s1, target_junction=j1b, mileage=WATARI_RAIL_B * 1 + STRAIGHT_RAIL * 1.5),
            stop_4: StopConfig(section=s3, target_junction=j0a, mileage=WATARI_RAIL_A * 1 + STRAIGHT_RAIL * 1.5),
        }
    )

    config.positions.update(
        {
            position_173: PositionConfig(
                section=s0, target_junction=j0b, mileage=WATARI_RAIL_B * 1 + STRAIGHT_RAIL * 2.5
            ),
            position_138: PositionConfig(
                section=s0,
                target_junction=j0b,
                mileage=WATARI_RAIL_B * 1 + STRAIGHT_RAIL * 9.5 + CURVE_RAIL * 8 + STRAIGHT_1_4_RAIL * 1,
            ),
            position_80: PositionConfig(
                section=s0,
                target_junction=j0b,
                mileage=WATARI_RAIL_B * 1 + STRAIGHT_RAIL * 13.5 + CURVE_RAIL * 8 + STRAIGHT_1_4_RAIL * 1,
            ),
            position_255: PositionConfig(
                section=s2,
                target_junction=j1a,
                mileage=WATARI_RAIL_A * 1 + STRAIGHT_RAIL * 5.5 + CURVE_RAIL * 8 + STRAIGHT_1_4_RAIL * 1,
            ),
        }
    )

    return config
