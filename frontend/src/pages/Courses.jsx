import React from 'react';
import { useState, useEffect } from 'react';
import CourseCard from '../components/Course/CourseCard';

export default function CoursesPage() {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/courses/')
      .then(res => res.json())
      .then(data => setCourses(data));
  }, []);

  return (
    <div>
      <h1>Courses</h1>
      {courses.map(course => (
        <CourseCard 
          key={course.id}
          title={course.title}
          description={course.description}
          creator={course.creator}
          duration={course.duration_minutes}
          tags={course.tags}
          created_at={course.created_at}
        />
      ))}
    </div>
  );
}