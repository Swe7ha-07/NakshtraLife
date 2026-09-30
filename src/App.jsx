import { useRef, useState } from "react";
import { Sun, Orbit, ClipboardCheck, LineChart, Lightbulb, SlidersHorizontal, Star, ScrollText, BookOpen, Sparkles, Moon, ChevronRight, Info, LogOut } from "lucide-react";
import useAppModel from "./appModel.js";
import StarField from "./components/StarField.jsx";
import Sidebar from "./components/Sidebar.jsx";
import MobileNav from "./components/MobileNav.jsx";
import Toast from "./components/Toast.jsx";
import TodayPage from "./pages/TodayPage.jsx";
import DigitalTwinPage from "./pages/DigitalTwinPage.jsx";
import CheckInPage from "./pages/CheckInPage.jsx";
import AnalyticsPage from "./pages/AnalyticsPage.jsx";
import RecommendationsPage from "./pages/RecommendationsPage.jsx";
import WhatIfPage from "./pages/WhatIfPage.jsx";
import MyStarRasiPage from "./pages/MyStarRasiPage.jsx";
import DailyPalanPage from "./pages/DailyPalanPage.jsx";
import IksContextPage from "./pages/IksContextPage.jsx";

const NAV = [
  { id: "today", label: "Today", icon: Sun, Page: TodayPage },
  { id: "twin", label: "Digital Twin", icon: Orbit, Page: DigitalTwinPage },
  { id: "checkin", label: "Check-in", icon: ClipboardCheck, Page: CheckInPage },
  { id: "analytics", label: "Analytics", icon: LineChart, Page: AnalyticsPage },
  { id: "recs", label: "Recommendations", icon: Lightbulb, Page: RecommendationsPage },
  { id: "whatif", label: "What-If", icon: SlidersHorizontal, Page: WhatIfPage },
  { id: "star", label: "My Star & Rasi", icon: Star, Page: MyStarRasiPage },
  { id: "palan", label: "Daily Palan", icon: ScrollText, Page: DailyPalanPage },
  { id: "iks", label: "IKS Context", icon: BookOpen, Page: IksContextPage },
];
const CITIES = ["Chennai", "Bengaluru", "Mumbai", "Delhi", "Coimbatore", "Madurai", "Singapore", "London", "New York"];

function ProfileSetup({ save }) {
  const [draft, setDraft] = useState({ name: "", email: "", birthDate: "", birthTime: "", birthCity: "Chennai", city: "Chennai" });
  const change = (key, value) => setDraft((old) => ({ ...old, [key]: value }));
  return <main className="login-shell">
    <div className="login-art"><div className="orbit orbit-a"/><div className="orbit orbit-b"/><div className="sun-core"><Sparkles size={25}/></div>
      <div className="art-copy"><div className="eyebrow">IKS · LIFESTYLE TWIN</div><h1>Your day,<br/><em>in living context.</em></h1><p>Connect traditional context with your changing daily routine.</p></div>
      <div className="art-foot">A tradition-led lifestyle companion · not a prediction</div>
    </div>
    <section className="form-side"><div className="brand"><div className="brand-icon"><Moon size={18}/></div><span>NakshatraLife Twin</span></div>
      <div className="form-wrap"><div className="eyebrow warm">CREATE YOUR DEMO PROFILE</div><h2>Start your Twin</h2><p className="muted">Birth date, time, and city are used to estimate your Nakshatra and Raasi.</p>
        <form onSubmit={(e) => { e.preventDefault(); save(draft); }}>
          <label>Your name<input required value={draft.name} onChange={(e) => change("name",e.target.value)} placeholder="e.g. Ananya"/></label>
          <label>Email<input required type="email" value={draft.email} onChange={(e) => change("email",e.target.value)} placeholder="you@example.com"/></label>
          <div className="row"><label>Birth date<input required type="date" value={draft.birthDate} onChange={(e) => change("birthDate",e.target.value)}/></label><label>Birth time<input required type="time" value={draft.birthTime} onChange={(e) => change("birthTime",e.target.value)}/></label></div>
          <div className="row">{[["birthCity","Birth city"],["city","Today's city"]].map(([key,label])=><label key={key}>{label}<select value={draft[key]} onChange={(e)=>change(key,e.target.value)}>{CITIES.map((city)=><option key={city}>{city}</option>)}</select></label>)}</div>
          <button className="primary">Create my Twin <ChevronRight size={17}/></button>
        </form>
        <div className="privacy"><Info size={15}/> Demo profile and lifestyle records stay in this browser.</div>
      </div><div className="disclaimer">Cultural information and habit reflection; not medical or scientific advice.</div>
    </section>
  </main>;
}

export default function App() {
  const model = useAppModel();
  const [page, setPage] = useState("today");
  const [toast, setToast] = useState(null);
  const timer = useRef(null);
  
  const notify = (msg) => { clearTimeout(timer.current); setToast({ msg, k: Date.now() }); timer.current = setTimeout(() => setToast(null), 4200); };
  if (!model.profile) return <ProfileSetup save={model.saveProfileData}/>;
  const current = NAV.find((n) => n.id === page) || NAV[0];
  const Page = current.Page;
  const navModel = { ...model, signOut: model.logout };
  return <div className="app">
    <StarField/>
    <Sidebar nav={NAV} page={page} setPage={setPage} profile={model.profile} onSignOut={model.logout}/>
    <button className="app-signout" onClick={model.logout} aria-label="Sign out"><LogOut size={16}/> Sign out</button>
    <main className="content" id="main">
      <div className="page" key={page}><Page model={navModel} notify={(message) => notify(message)} goTo={setPage} title={current.label}/></div>
      <p className="disclaimer">{model.disclaimer}</p>
    </main>
    <MobileNav nav={NAV} page={page} setPage={setPage}/><Toast toast={toast}/>
  </div>;
}
