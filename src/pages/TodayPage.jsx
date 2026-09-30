import { Clock, Sparkles, Orbit } from "lucide-react";
import PageHeader from "../components/PageHeader.jsx";
import Card from "../components/Card.jsx";
import OrbitScore from "../components/OrbitScore.jsx";

export default function TodayPage({ model, title, goTo }) {
  const { date, setDate, panchangam, palan, twin, profile } = model;
  return (
    <>
      <PageHeader title={title} subtitle="Estimated time windows and a traditional reading for your day." date={date} setDate={setDate} />
      <div className="grid two">
        <Card title="Panchangam windows (estimated)" icon={Clock} hero i={0}>
          {panchangam.map((w) => (
            <div className="window-row" key={w.label}>
              <span>{w.label}{w.note && <small className="muted"> · {w.note}</small>}</span>
              <b>{w.start} – {w.end}</b>
            </div>
          ))}
        </Card>
        <Card title="Digital Twin routine" icon={Orbit} i={1}>
          <OrbitScore value={twin.score} />
          <p className="muted" style={{ textAlign: "center" }}>{twin.summary}</p>
          <div className="btn-row" style={{ justifyContent: "center" }}>
            <button className="btn" onClick={() => goTo("checkin")}>Add check-in</button>
          </div>
        </Card>
      </div>
      <div style={{ marginTop: 18 }}>
        <Card title={`Raasi / Star Palan · ${profile.raasi}`} icon={Sparkles} i={2}>
          <div className="grid two" style={{ marginTop: 8 }}>
            {palan.sections.map((s) => (
              <div key={s.title}><span className="tag">{s.title}</span><p>{s.text}</p></div>
            ))}
          </div>
          {palan.avoid && <p style={{ marginTop: 12 }}><span className="tag">Things to avoid</span> {palan.avoid}</p>}
          <div className="btn-row">
            {palan.links?.map((l) => (
              <a key={l.url} className="btn" href={l.url} target="_blank" rel="noreferrer">{l.label}</a>
            ))}
          </div>
        </Card>
      </div>
    </>
  );
}
