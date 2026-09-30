import { CheckCircle2 } from "lucide-react";

export default function Toast({ toast }) {
  return (
    <div aria-live="polite" role="status">
      {toast && (
        <div className="toast" key={toast.k}>
          <CheckCircle2 size={20} color="var(--gold)" />{toast.msg}
        </div>
      )}
    </div>
  );
}
