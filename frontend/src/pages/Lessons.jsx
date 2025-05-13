import React from 'react';
import { useState, useEffect } from 'react';
import LessonCard from '../components/LessonCard';

export default function LessonsPage({ course_id }) {
  const [lessons, setLessons] = useState([]);

  useEffect(() => {
    fetch(`http://localhost:8000/api/courses/${course_id}/lessons/`)
      .then(res => res.json())
      .then(data => setLessons(data));
  }, [course_id]);

  return (
    <div>
      <h1>Lessons</h1>
      {lessons.map(lesson => (
        <LessonCard 
          key={lesson.id}
          title={lesson.title}
          content={lesson.content}
          video_url={lesson.video_url}
          order={lesson.order}
        />
      ))}
    </div>
  );
}