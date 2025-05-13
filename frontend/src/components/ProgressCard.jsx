export default function ProgressCard({ course, completed_lessons, completed_at }) {
    const totalLessons = course.lessons_count || 0;
    const completedCount = completed_lessons.length;
    const progressPercentage = totalLessons > 0 
      ? Math.round((completedCount / totalLessons) * 100) 
      : 0;
  
    return (
      <div className="progress-card">
        <h2>{course.title}</h2>
        <div className="progress-bar">
          <div 
            className="progress-fill" 
            style={{ width: `${progressPercentage}%` }}
          >
            {progressPercentage}%
          </div>
        </div>
        <p>
          Completed {completedCount} of {totalLessons} lessons
        </p>
        {completed_at && (
          <p className="completion-date">
            Completed on: {new Date(completed_at).toLocaleDateString()}
          </p>
        )}
      </div>
    );
  }