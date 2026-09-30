import PageHeader from "../components/PageHeader.jsx";
import Card from "../components/Card.jsx";
import OrbitScore from "../components/OrbitScore.jsx";

export default function WhatIfPage({ model, title }) {
  const { whatIf, twin } = model;
  const labels = { sleep: "Sleep", activity: "Movement", study: "Focused learning", water: "Water" };
  return (
    <>
      <PageHeader title={title} subtitle="Explore how a small change could move your routine score." />
      <div className="grid two">
        <Card title="Scenario" hero i={0}>
          <label>Routine measure
            <select value={whatIf.metric} onChange={(e) => whatIf.setMetric(e.target.value)}>
              {Object.entries(labels).map(([key, label]) => <option value={key} key={key}>{label}</option>)}
            </select>
          </label>
          <label style={{ marginTop: 14 }}>{whatIf.label}
            <input type="range" min={whatIf.min} max={whatIf.max} step={whatIf.step} value={whatIf.value} onChange={(e) => whatIf.setValue(Number(e.target.value))} />
          </label>
          <p className="muted">Add {whatIf.value} {whatIf.unit} to the recent daily average.</p>
        </Card>
        <Card title="Projection" i={1}>
          <OrbitScore value={whatIf.projected.toFixed(1)} label="Projected" />
          <p className="muted" style={{ textAlign: "center" }}>Current: {whatIf.current.toFixed(1)}</p>
          {whatIf.atGoal && <p className="scenario-note">This measure is already at or above its reference goal, so its score contribution is capped.</p>}
          <p className="scenario-note">The change is added to the recent average for the selected measure; the score is recalculated immediately.</p>
        </Card>
      </div>
    </>
  );
}
