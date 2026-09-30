import PageHeader from "../components/PageHeader.jsx";
import Card from "../components/Card.jsx";
import OrbitScore from "../components/OrbitScore.jsx";

export default function MyStarRasiPage({ model, title }) {
  const s = model.starInfo;
  return (
    <>
      <PageHeader title={title} subtitle="Estimated from your birth details; not an authoritative chart." />
      <div className="grid two">
        <Card hero i={0}>
          <OrbitScore label="Pada"><b>{s.pada}</b><small>{s.nakshatra}</small></OrbitScore>
        </Card>
        <Card title="Your estimate" i={1}>
          <p><span className="tag">Nakshatra</span> {s.nakshatra}</p>
          <p><span className="tag">Pada</span> {s.pada}</p>
          <p><span className="tag">Janma Raasi</span> {s.raasi}</p>
        </Card>
      </div>
      <div className="stack" style={{ marginTop: 18 }}>
        {s.notes.map((n, i) => <Card key={i} i={i + 2}><p>{n}</p></Card>)}
      </div>
    </>
  );
}
