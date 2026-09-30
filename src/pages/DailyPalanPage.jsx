import PageHeader from "../components/PageHeader.jsx";
import Card from "../components/Card.jsx";

export default function DailyPalanPage({ model, title }) {
  const { date, setDate, palan } = model;
  return (
    <>
      <PageHeader title={title} subtitle="A traditional reading for the selected date." date={date} setDate={setDate} />
      <div className="grid two">
        {palan.sections.map((s, i) => (
          <Card key={s.title} title={s.title} i={i}><p className="muted">{s.text}</p></Card>
        ))}
      </div>
      {palan.avoid && (
        <div style={{ marginTop: 18 }}>
          <Card title="Things to avoid" i={5}><p>{palan.avoid}</p></Card>
        </div>
      )}
      <div className="btn-row">
        {palan.links?.map((l) => (
          <a key={l.url} className="btn" href={l.url} target="_blank" rel="noreferrer">{l.label}</a>
        ))}
      </div>
    </>
  );
}
