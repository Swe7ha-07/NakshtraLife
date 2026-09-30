import PageHeader from "../components/PageHeader.jsx";
import Card from "../components/Card.jsx";

const FIELDS = [
  ["sleep", "Sleep (hours)", { step: 0.5, min: 0, max: 24 }],
  ["movement", "Movement (minutes)", { step: 5, min: 0 }],
  ["learning", "Focused learning (minutes)", { step: 5, min: 0 }],
  ["water", "Water (glasses)", { step: 1, min: 0 }],
];

export default function CheckInPage({ model, notify, goTo, title }) {
  const { form, setForm, saveCheckin } = model;
  const submit = (e) => {
    e.preventDefault();
    saveCheckin();
    notify("Check-in saved — your Digital Twin has been updated.");
    goTo("twin");
  };
  return (
    <>
      <PageHeader title={title} subtitle="Record today's routine. Data stays in this browser." />
      <Card hero i={0}>
        <form onSubmit={submit} className="stack">
          <div className="form-grid">
            {FIELDS.map(([k, label, attrs]) => (
              <label key={k}>{label}
                <input type="number" inputMode="decimal" {...attrs} value={form[k]}
                  onChange={(e) => setForm({ ...form, [k]: e.target.value })} />
              </label>
            ))}
          </div>
          <div><button className="btn primary" type="submit">Save check-in</button></div>
        </form>
      </Card>
    </>
  );
}
