export default function Card({ title, icon: Icon, hero, i = 0, children, className = "" }) {
  return (
    <section className={`card ${hero ? "hero" : ""} ${className}`} style={{ "--i": i }}>
      {title && (
        <h3>
          {Icon && <Icon size={18} style={{ marginRight: 8, verticalAlign: "-2px", color: "var(--gold)" }} />}
          {title}
        </h3>
      )}
      {children}
    </section>
  );
}
