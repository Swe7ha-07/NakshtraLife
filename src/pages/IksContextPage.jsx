import PageHeader from "../components/PageHeader.jsx";
import Card from "../components/Card.jsx";

export default function IksContextPage({ model, title }) {
  return (
    <>
      <PageHeader title={title} subtitle="Nakshatra, Panchanga, Dinacharya and Ritucharya." />
      <div className="grid two">
        {model.iks.map((c, i) => <Card key={c.title} title={c.title} i={i}><p className="muted">{c.text}</p></Card>)}
      </div>
    </>
  );
}
