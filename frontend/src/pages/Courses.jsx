import React from 'react';
import { useState, useEffect } from 'react';
import CourseCard from '../components/Course/CourseCard';

export default function CoursesPage() {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    console.log('Загружаем курсы...');
    const fetchCourses = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/courses/');
        const data = await response.json();
        console.log('Полученные курсы:', data);
        setCourses(data);
      } catch (e) {
        console.error(e);
      } finally {
        setLoading(false);
      }
    };
  
    fetchCourses();
  }, []);

  return (
    <div>
      <h1>Courses</h1>
      {courses.map(course => (
      <CourseCard
        key={course.id}
        courseId={course.id} 
        title={course.title}
        description={course.description}
        creator={course.creator}
        duration_minutes={course.duration_minutes}
        tags={course.tags || []}
        created_at={course.created_at}
      />
))}
    </div>
  );
}