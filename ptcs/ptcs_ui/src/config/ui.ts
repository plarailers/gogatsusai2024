import { DEFAULT_THEME } from "@mantine/core";
import { RailwayUI } from "../types";

export const ui: RailwayUI = {
  width: 2000,
  height: 720,
  platforms: {
    p00: { position: { x: 300, y: 280 } },
    p01: { position: { x: 300, y: 440 } },
    p02: { position: { x: 580, y: 200 } },
    p03: { position: { x: 580, y: 520 } },
    p04: { position: { x: 860, y: 200 } },
    p05: { position: { x: 860, y: 440 } },
    p06: { position: { x: 1140, y: 200 } },
    p07: { position: { x: 1140, y: 520 } },
    p08: { position: { x: 1420, y: 200 } },
    p09: { position: { x: 1420, y: 360 } },
    p10: { position: { x: 1420, y: 520 } },
    p11: { position: { x: 1700, y: 280 } },
    p12: { position: { x: 1700, y: 440 } },
  },
  junctions: {
    j00: { position: { x: 400, y: 240 } },
    j01: { position: { x: 440, y: 320 } },
    j02: { position: { x: 480, y: 320 } },
    j03: { position: { x: 520, y: 240 } },
    j04: { position: { x: 760, y: 320 } },
    j05: { position: { x: 1000, y: 240 } },
    j06: { position: { x: 1040, y: 240 } },
    j07: { position: { x: 1080, y: 320 } },
    j08: { position: { x: 1640, y: 400 } },
    j09: { position: { x: 1600, y: 480 } },
    j10: { position: { x: 1560, y: 480 } },
    j11: { position: { x: 1520, y: 400 } },
    j12: { position: { x: 1040, y: 480 } },
    j13: { position: { x: 1000, y: 400 } },
    j14: { position: { x: 960, y: 400 } },
    j15: { position: { x: 920, y: 480 } },
  },
  sections: {
    s00: {
      from: "j00",
      to: "j01",
      points: [
        { x: 400, y: 240 },
        { x: 440, y: 320 },
      ],
    },
    s01: {
      from: "j00",
      to: "j03",
      points: [
        { x: 400, y: 240 },
        { x: 520, y: 240 },
      ],
    },
    s02: {
      from: "j01",
      to: "j02",
      points: [
        { x: 440, y: 320 },
        { x: 480, y: 320 },
      ],
    },
    s03: {
      from: "j02",
      to: "j03",
      points: [
        { x: 480, y: 320 },
        { x: 520, y: 240 },
      ],
    },
    s04: {
      from: "j02",
      to: "j04",
      points: [
        { x: 480, y: 320 },
        { x: 760, y: 320 },
      ],
    },
    s05: {
      from: "j03",
      to: "j05",
      points: [
        { x: 520, y: 240 },
        { x: 720, y: 240 },
        { x: 760, y: 160 },
        { x: 960, y: 160 },
        { x: 1000, y: 240 },
      ],
    },
    s06: {
      from: "j04",
      to: "j05",
      points: [
        { x: 760, y: 320 },
        { x: 800, y: 240 },
        { x: 1000, y: 240 },
      ],
    },
    s07: {
      from: "j04",
      to: "j07",
      points: [
        { x: 760, y: 320 },
        { x: 1080, y: 320 },
      ],
    },
    s08: {
      from: "j05",
      to: "j06",
      points: [
        { x: 1000, y: 240 },
        { x: 1040, y: 240 },
      ],
    },
    s09: {
      from: "j06",
      to: "j07",
      points: [
        { x: 1040, y: 240 },
        { x: 1080, y: 320 },
      ],
    },
    s10: {
      from: "j06",
      to: "j09",
      points: [
        { x: 1040, y: 240 },
        { x: 1920, y: 240 },
        { x: 1920, y: 480 },
        { x: 1600, y: 480 },
      ],
    },
    s11: {
      from: "j07",
      to: "j08",
      points: [
        { x: 1080, y: 320 },
        { x: 1840, y: 320 },
        { x: 1840, y: 400 },
        { x: 1640, y: 400 },
      ],
    },
    s12: {
      from: "j08",
      to: "j09",
      points: [
        { x: 1640, y: 400 },
        { x: 1600, y: 480 },
      ],
    },
    s13: {
      from: "j08",
      to: "j11",
      points: [
        { x: 1640, y: 400 },
        { x: 1520, y: 400 },
      ],
    },
    s14: {
      from: "j09",
      to: "j10",
      points: [
        { x: 1600, y: 480 },
        { x: 1560, y: 480 },
      ],
    },
    s15: {
      from: "j10",
      to: "j11",
      points: [
        { x: 1560, y: 480 },
        { x: 1520, y: 400 },
      ],
    },
    s16: {
      from: "j10",
      to: "j12",
      points: [
        { x: 1560, y: 480 },
        { x: 1040, y: 480 },
      ],
    },
    s17: {
      from: "j11",
      to: "j13",
      points: [
        { x: 1520, y: 400 },
        { x: 1000, y: 400 },
      ],
    },
    s18: {
      from: "j12",
      to: "j13",
      points: [
        { x: 1040, y: 480 },
        { x: 1000, y: 400 },
      ],
    },
    s19: {
      from: "j12",
      to: "j15",
      points: [
        { x: 1040, y: 480 },
        { x: 920, y: 480 },
      ],
    },
    s20: {
      from: "j13",
      to: "j14",
      points: [
        { x: 1000, y: 400 },
        { x: 960, y: 400 },
      ],
    },
    s21: {
      from: "j14",
      to: "j15",
      points: [
        { x: 960, y: 400 },
        { x: 920, y: 480 },
      ],
    },
    s22: {
      from: "j14",
      to: "j01",
      points: [
        { x: 960, y: 400 },
        { x: 160, y: 400 },
        { x: 160, y: 320 },
        { x: 440, y: 320 },
      ],
    },
    s23: {
      from: "j15",
      to: "j00",
      points: [
        { x: 920, y: 480 },
        { x: 80, y: 480 },
        { x: 80, y: 240 },
        { x: 400, y: 240 },
      ],
    },
  },
  trains: {
    t0: {
      fill: DEFAULT_THEME.colors.blue[4],
      stroke: DEFAULT_THEME.colors.blue[9],
    },
    t1: {
      fill: DEFAULT_THEME.colors.orange[5],
      stroke: DEFAULT_THEME.colors.orange[9],
    },
    t2: {
      fill: DEFAULT_THEME.colors.indigo[6],
      stroke: DEFAULT_THEME.colors.indigo[9],
    },
    t3: {
      fill: DEFAULT_THEME.colors.lime[5],
      stroke: DEFAULT_THEME.colors.lime[9],
    },
    t4: {
      fill: DEFAULT_THEME.colors.red[5],
      stroke: DEFAULT_THEME.colors.red[9],
    },
  },
  stops: {
    // stop_0: {},
    // stop_1: {},
  },
  obstacles: {
    // obstacle_0: {},
  },
};
