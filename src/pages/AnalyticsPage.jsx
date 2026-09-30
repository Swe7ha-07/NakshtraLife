import PageHeader from "../components/PageHeader.jsx";
import Card from "../components/Card.jsx";
import MetricCard from "../components/MetricCard.jsx";
import TrendChart from "../components/TrendChart.jsx";

export default function AnalyticsPage({ model, title }) {
  const { twin, checkins } = model;
  const recent = checkins.slice(-7);
  return (
    <>
      <PageHeader title={title} subtitle="Seven-day averages and recent history." />
      <div className="grid">
        <MetricCard i={0} label="Sleep avg" value={twin.sleep} unit="h" />
        <MetricCard i={1} label="Movement avg" value={twin.movement} unit="min" />
        <MetricCard i={2} label="Learning avg" value={twin.learning} unit="min" />
        <MetricCard i={3} label="Water avg" value={twin.water} unit="glasses" />
      </div>
      <div className="stack" style={{ marginTop: 18 }}>
        <Card title="Sleep trend" i={4}>
          <TrendChart points={recent.map((c) => Number(c.sleep))} labels={recent.map((c) => String(c.date).slice(5))} />
        </Card>
        <Card title="Recent check-ins" i={5}>
          <div className="table-wrap">
            <table>
              <thead><tr><th>Date</th><th>Sleep</th><th>Move</th><th>Learn</th><th>Water (glasses)</th></tr></thead>
              <tbody>
                {[...checkins].reverse().slice(0, 10).map((c) => (
                  <tr key={c.date}><td>{c.date}</td><td>{c.sleep}</td><td>{c.movement}</td><td>{c.learning}</td><td>{c.water}</td></tr>
                ))}
              </tbody>
            </table>
          </div>
        </Card>
      </div>
    </>
  );
}
