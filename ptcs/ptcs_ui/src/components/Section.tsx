import { useContext } from "react";
import { RailwayStateContext } from "../contexts";

interface SectionProps {
  id: string;
  points: { x: number; y: number }[];
}

export const Section: React.FC<SectionProps> = ({ id, points }) => {
  const railwayState = useContext(RailwayStateContext);

  if (!railwayState) return null;

  const sectionState = railwayState.sections[id];

  const shrunkPointFirst = shrink(points[0], points[1], 4);

  const n = points.length;

  const shrunkPointLast = shrink(points[n - 1], points[n - 2], 4);

  const shrunkPoints = [
    shrunkPointFirst,
    ...points.slice(1, -1),
    shrunkPointLast,
  ];

  return (
    <polyline
      points={shrunkPoints.map((p) => `${p.x},${p.y}`).join(" ")}
      fill="none"
      stroke={sectionState.is_blocked ? "red" : "white"}
      strokeWidth={sectionState.is_blocked ? 4 : 2}
      strokeLinecap="square"
    />
  );
};

const shrink = (
  p: { x: number; y: number },
  q: { x: number; y: number },
  amount: number
): { x: number; y: number } => {
  return {
    x: p.x + ((q.x - p.x) / Math.hypot(q.x - p.x, q.y - p.y)) * amount,
    y: p.y + ((q.y - p.y) / Math.hypot(q.x - p.x, q.y - p.y)) * amount,
  };
};
