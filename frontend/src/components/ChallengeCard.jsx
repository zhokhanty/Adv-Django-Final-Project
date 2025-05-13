export default function ChallengeCard({ 
    title, 
    description, 
    days, 
    tags, 
    created_at 
  }) {
    return (
      <div className="challenge-card">
        <h2>{title}</h2>
        <p className="description">{description}</p>
        <div className="challenge-meta">
          <span className="duration">{days}-day challenge</span>
          <span className="created-date">
            Started {new Date(created_at).toLocaleDateString()}
          </span>
        </div>
        <div className="tags">
          {tags.map((tag, index) => (
            <span key={index} className="tag">{tag}</span>
          ))}
        </div>
        <button className="join-button">Join Challenge</button>
      </div>
    );
  }