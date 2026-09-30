import Card from "./Card.jsx";

export default function MetricCard({ label, value, unit, pct, i }) {
  return (
    <Card i={i} className="metric">
      <div className="label">{label}</div>
      <div><span className="value">{value}</span>{unit && <span className="unit">{unit}</span>}</div>
      {pct != null && (
        <div className="bar" role="presentation">
          <i style={{ width: `${Math.max(0, Math.min(100, pct))}%` }} />
        </div>
      )}
    </Card>
  );
}
