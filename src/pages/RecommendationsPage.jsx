import { Lightbulb } from "lucide-react";
import PageHeader from "../components/PageHeader.jsx";
import Card from "../components/Card.jsx";

const OPTS = [["Helpful", "Helpful"], ["Not helpful", "Not helpful"], ["Later", "Later"]];

export default function RecommendationsPage({ model, title }) {
  const { recs, feedback, setFeedback } = model;
  return (
    <>
      <PageHeader title={title} subtitle="Rule-based suggestions from your recent routine." />
      <div className="stack">
        {recs.map((r, i) => (
          <Card key={r.id} title={r.title} icon={Lightbulb} i={i}>
            <p className="muted">{r.text}</p>
            <div className="btn-row" role="group" aria-label={`Feedback for ${r.title}`}>
              {OPTS.map(([v, l]) => (
                <button key={v} className={`btn ${feedback[r.metric] === v ? "on" : ""}`}
                  aria-pressed={feedback[r.metric] === v} onClick={() => setFeedback(r.metric, v)}>{l}</button>
              ))}
            </div>
          </Card>
        ))}
      </div>
    </>
  );
}
