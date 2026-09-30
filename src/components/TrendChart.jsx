export default function TrendChart({ points, labels = [], height = 180, stroke = "var(--gold)" }) {
  const W = 600, H = height, pad = 24;
  if (!points?.length) return <p className="muted">No data yet.</p>;
  const max = Math.max(...points, 1), min = Math.min(...points, 0);
  const x = (i) => pad + (points.length === 1 ? (W - 2 * pad) / 2 : (i * (W - 2 * pad)) / (points.length - 1));
  const y = (v) => H - pad - ((v - min) / (max - min || 1)) * (H - 2 * pad);
  const d = points.map((v, i) => `${i ? "L" : "M"}${x(i)},${y(v)}`).join(" ");
  return (
    <svg className="chart" viewBox={`0 0 ${W} ${H}`} role="img" aria-label="Trend chart">
      {[0, 0.5, 1].map((t) => (
        <line key={t} className="grid-line" x1={pad} x2={W - pad} y1={pad + t * (H - 2 * pad)} y2={pad + t * (H - 2 * pad)} />
      ))}
      <path key={d} className="line" d={d} pathLength="1" fill="none" stroke={stroke} strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
      {points.map((v, i) => <circle key={i} cx={x(i)} cy={y(v)} r="3.5" fill={stroke} />)}
      {labels.map((l, i) => <text key={i} className="axis" x={x(i)} y={H - 6} textAnchor="middle">{l}</text>)}
    </svg>
  );
}
