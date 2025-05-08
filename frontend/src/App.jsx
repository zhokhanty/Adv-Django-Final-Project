import { useState, useEffect } from 'react';
import Course from './components/Course';
import Login from './components/Login';
import Register from './components/Register';

function App() {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/course/')
      .then(res => res.json())
      .then(data => setCourses(data));
  }, []);

  return (
    <div>
      <h1>Auth Demo</h1>
      <Login />
      <hr />
      <Register />
      <h1>Courses</h1>
      {courses.map(course => (
        <Course
          key={course.id}
          title={course.title}
          description={course.description}
          duration={course.duration_minutes}
          tags={course.tags}
        />
      ))}
    </div>
  );
}

export default App;
