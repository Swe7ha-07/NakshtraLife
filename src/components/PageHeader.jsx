export default function PageHeader({ title, subtitle, date, setDate }) {
  return (
    <header className="page-header">
      <div>
        <div className="eyebrow">NakshatraLife Twin</div>
        <h1>{title}</h1>
        {subtitle && <p>{subtitle}</p>}
      </div>
      {setDate && (
        <label>Date
          <input className="date-control" type="date" value={date} onChange={(e) => setDate(e.target.value)} />
        </label>
      )}
    </header>
  );
}
