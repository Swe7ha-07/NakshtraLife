import { Sparkles, MapPin, LogOut } from "lucide-react";

export default function Sidebar({ nav, page, setPage, profile, onSignOut }) {
  return (
    <aside className="sidebar">
      <div className="brand"><Sparkles size={22} /> NakshatraLife</div>
      <div className="profile-chip">
        <strong>{profile?.name || "Your profile"}</strong>
        <span>{profile?.nakshatra} · {profile?.raasi}</span><br />
        <span><MapPin size={12} style={{ verticalAlign: "-1px" }} /> {profile?.city}</span>
      </div>
      <nav className="nav" aria-label="Sections">
        {nav.map(({ id, label, icon: Icon }) => (
          <button key={id} onClick={() => setPage(id)} aria-current={page === id ? "page" : undefined}>
            <Icon size={18} /> {label}
          </button>
        ))}
      </nav>
      <button className="sidebar-logout" onClick={onSignOut}><LogOut size={16}/> Sign out</button>
    </aside>
  );
}
