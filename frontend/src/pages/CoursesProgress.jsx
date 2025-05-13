import React from 'react';
import { useState, useEffect } from 'react';
import ProgressCard from '../components/ProgressCard';

export default function CourseProgressPage() {
  const [progresses, setProgresses] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/course-progress/', {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      }
    })
      .then(res => res.json())
      .then(data => setProgresses(data));
  }, []);

  return (
    <div>
      <h1>My Course Progress</h1>
      {progresses.map(progress => (
        <ProgressCard 
          key={progress.id}
          course={progress.course}
          completed_lessons={progress.completed_lessons}
          completed_at={progress.completed_at}
        />
      ))}
    </div>
  );
}