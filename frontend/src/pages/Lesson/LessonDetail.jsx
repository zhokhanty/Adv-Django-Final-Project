import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import './LessonDetail.css';

export default function LessonDetailPage() {
  const { courseId, lessonId } = useParams();
  const [lesson, setLesson] = useState(null);
  const [loading, setLoading] = useState(true);
  const markAsComplete = async () => {
    try {
      const response = await fetch(`http://localhost:8000/api/course/${courseId}/lesson/${lessonId}/complete/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${localStorage.getItem('access')}`,
        },
      });
  
        if (!response.ok) {
            throw new Error('Error to finish lesson');
        }

        const data = await response.json();
        console.log('Lesson is finish:', data);
    } catch (error) {
      console.error('Error:', error);
      alert(error.message);
    }
  };  

  useEffect(() => {
    const fetchLesson = async () => {
      try {
        const response = await fetch(`http://localhost:8000/api/course/${courseId}/lesson/${lessonId}/`);
        if (!response.ok) throw new Error('Ошибка загрузки урока');
        const data = await response.json();
        setLesson(data);
      } catch (error) {
        console.error('Ошибка при получении урока:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchLesson();
  }, [courseId, lessonId]);

  if (loading) return <div>Loading...</div>;

  if (!lesson) return <div>Lesson not found.</div>;

  return (
    <div className="lesson-detail-container">
      <h2 className="lesson-title">{lesson.title}</h2>
      <p className="lesson-content">{lesson.content}</p>

      {lesson.video_url && (
        <div className="video-section">
          <h4>Video:</h4>
          <video controls>
            <source src={lesson.video_url} type="video/mp4" />
          </video>
        </div>
      )}
      <button
        onClick={markAsComplete}
        style={{
            marginTop: '20px',
            padding: '10px 20px',
            backgroundColor: '#4f46e5',
            color: 'white',
            border: 'none',
            borderRadius: '5px',
            cursor: 'pointer'
        }}
        >
        Finish the lesson
        </button>

    </div>
  );
}
