export default function LessonCard({ title, content, video_url, order }) {
    return (
      <div className="lesson-card">
        <h2>Lesson {order}: {title}</h2>
        <div className="lesson-content">
          <p>{content}</p>
        </div>
        {video_url && (
          <div className="video-container">
            <iframe 
              src={video_url} 
              title={title}
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            />
          </div>
        )}
      </div>
    );
  }