import { DEFAULT_THEME } from "@mantine/core";
import { RailwayUI } from "../types";

export const ui: RailwayUI = {
  width: 440,
  height: 340,
  platforms: {},
  junctions: {
    j0: { position: { x: 400, y: 160 } },
    j1: { position: { x: 360, y: 200 } },
    j2: { position: { x: 280, y: 280 } },
    j3: { position: { x: 260, y: 300 } },
  },
  sections: {
    s0: {
      from: "j0",
      to: "j3",
      points: [
        { x: 400, y: 160 },
        { x: 400, y: 280 },
        { x: 380, y: 300 },
        { x: 260, y: 300 },
      ],
    },
    s1: {
      from: "j3",
      to: "j0",
      points: [
        { x: 260, y: 300 },
        { x: 60, y: 300 },
        { x: 40, y: 280 },
        { x: 40, y: 220 },
        { x: 220, y: 40 },
        { x: 380, y: 40 },
        { x: 400, y: 60 },
        { x: 400, y: 160 },
      ],
    },
    s2: {
      from: "j1",
      to: "j2",
      points: [
        { x: 360, y: 200 },
        { x: 360, y: 250 },
        { x: 330, y: 280 },
        { x: 280, y: 280 },
      ],
    },
    s3: {
      from: "j2",
      to: "j1",
      points: [
        { x: 280, y: 280 },
        { x: 110, y: 280 },
        { x: 80, y: 250 },
        { x: 80, y: 110 },
        { x: 110, y: 80 },
        { x: 330, y: 80 },
        { x: 360, y: 110 },
        { x: 360, y: 200 },
      ],
    },
    s4: {
      from: "j0",
      to: "j1",
      points: [
        { x: 400, y: 160 },
        { x: 360, y: 200 },
      ],
    },
    s5: {
      from: "j2",
      to: "j3",
      points: [
        { x: 280, y: 280 },
        { x: 260, y: 300 },
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
    stop_0: {},
    stop_1: {},
  },
  obstacles: {
    obstacle_0: {},
  },
};