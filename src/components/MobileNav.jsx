const SHORT = { "My Star & Rasi": "Star", "Recommendations": "Tips", "Digital Twin": "Twin" };

export default function MobileNav({ nav, page, setPage }) {
  return (
    <nav className="mobile-nav" aria-label="Sections">
      {nav.map(({ id, label, icon: Icon }) => (
        <button key={id} onClick={() => setPage(id)} aria-current={page === id ? "page" : undefined}>
          <Icon size={20} /><span>{SHORT[label] || label}</span>
        </button>
      ))}
    </nav>
  );
}
