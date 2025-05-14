import { useParams, useNavigate, Link } from 'react-router-dom';
import { useEffect, useState } from 'react';
import './Lessons.css';

export default function LessonsPage() {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const [lessons, setLessons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [progress, setProgress] = useState([]);

  useEffect(() => {
    const fetchProgress = async () => {
      try {
        const response = await fetch(`http://localhost:8000/api/course/${courseId}/progress/`, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access')}`,
          }
        });
        if (!response.ok) throw new Error('Ошибка загрузки прогресса');
        const data = await response.json();
        setProgress(data);
      } catch (error) {
        console.error('Ошибка прогресса:', error);
      }
    };

    fetchProgress();
  }, [courseId]);

  useEffect(() => {
    if (!courseId || isNaN(Number(courseId))) {
      navigate('/courses');
      return;
    }

    const fetchLessons = async () => {
      try {
        const response = await fetch(`http://localhost:8000/api/course/${courseId}/lessons/`);
        if (!response.ok) throw new Error('Ошибка загрузки уроков');
        const data = await response.json();
        setLessons(data);
      } catch (error) {
        console.error('Ошибка при получении уроков:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchLessons();
  }, [courseId, navigate]);

  if (loading) return <div className="loading">Загрузка...</div>;

  return (
    <div className="lessons-container">
      <h2 className="lessons-title">Список уроков</h2>
      {lessons.length === 0 ? (
        <p className="no-lessons">Нет доступных уроков.</p>
      ) : (
        <ul className="lesson-list">
          {lessons.map(lesson => (
            <li key={lesson.id} className="lesson-item">
              <Link to={`/courses/${courseId}/lesson/${lesson.id}`} className="lesson-link">
                {lesson.order}. {lesson.title}
              </Link>
            </li>
          ))}
        </ul>
      )}
      {progress && (
      <div style={{ marginBottom: '20px' }}>
        <p style={{ fontSize: '16px', fontWeight: '500' }}>
          Прогресс: {progress.completed_lessons} из {lessons.length}
        </p>
      </div>
      )}

    </div>
  );
}
