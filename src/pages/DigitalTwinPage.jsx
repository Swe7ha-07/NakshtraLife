import PageHeader from "../components/PageHeader.jsx";
import Card from "../components/Card.jsx";
import MetricCard from "../components/MetricCard.jsx";
import OrbitScore from "../components/OrbitScore.jsx";

// Bar scales below are visual only. Replace with your app's targets if you have them.
export default function DigitalTwinPage({ model, title }) {
  const t = model.twin;
  return (
    <>
      <PageHeader title={title} subtitle="Your routine, reflected as a living model." />
      <Card hero i={0}><OrbitScore value={t.score} label="Consistency" /></Card>
      <div className="grid" style={{ marginTop: 18 }}>
        <MetricCard i={1} label="Sleep" value={t.sleep} unit="h" pct={(t.sleep / 9) * 100} />
        <MetricCard i={2} label="Movement" value={t.movement} unit="min" pct={(t.movement / 60) * 100} />
        <MetricCard i={3} label="Focused learning" value={t.learning} unit="min" pct={(t.learning / 120) * 100} />
        <MetricCard i={4} label="Water" value={t.water} unit="glasses" pct={(t.water / 8) * 100} />
      </div>
    </>
  );
}
