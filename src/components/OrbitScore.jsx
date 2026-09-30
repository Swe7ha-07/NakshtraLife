export default function OrbitScore({ value, label = "Routine score", children }) {
  return (
    <div className="orbit" role="img" aria-label={`${label}: ${value ?? ""}`}>
      <div className="ring"><span className="dot" /></div>
      <div className="ring r2">
        <span className="dot" style={{ background: "var(--aurora-b)", boxShadow: "0 0 12px var(--aurora-b)" }} />
      </div>
      <div className="core">{children || (<><b>{value}</b><small>{label}</small></>)}</div>
    </div>
  );
}
