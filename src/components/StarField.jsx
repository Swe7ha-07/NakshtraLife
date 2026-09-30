import { useMemo } from "react";

export default function StarField() {
  const stars = useMemo(() => Array.from({ length: 70 }, (_, i) => ({
    i, x: Math.random() * 100, y: Math.random() * 100,
    s: Math.random() < 0.15 ? 2.5 : 1.3, d: 3 + Math.random() * 5, delay: Math.random() * 5,
  })), []);
  return (
    <div className="starfield" aria-hidden="true">
      <div className="layer">
        {stars.map((s) => (
          <span key={s.i} className="star"
            style={{ left: `${s.x}%`, top: `${s.y}%`, width: s.s, height: s.s, "--d": `${s.d}s`, "--delay": `${s.delay}s` }} />
        ))}
      </div>
    </div>
  );
}
