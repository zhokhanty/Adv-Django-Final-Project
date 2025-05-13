export default function ChallengeProgressCard({ challenge, current_day, completed_days, started_at, completed_at }) {
    return (
      <div className="challenge-progress-card">
        <h2>{challenge.title}</h2>
        <p>Current Day: {current_day} of {challenge.days}</p>
        <p>Completed Days: {completed_days.length}</p>
        <progress value={completed_days.length} max={challenge.days} />
        <p>Started: {new Date(started_at).toLocaleDateString()}</p>
        {completed_at && <p>Completed: {new Date(completed_at).toLocaleDateString()}</p>}
      </div>
    );
  }