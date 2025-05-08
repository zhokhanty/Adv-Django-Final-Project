import React from 'react';

function Course({ title, description, duration, tags }) {
  return (
    <div className="course-card">
      <h2>{title}</h2>
      <p>{description}</p>
      <p><strong>Duration:</strong> {duration} minutes</p>
      <p><strong>Tags:</strong> {tags?.join(', ')}</p>
    </div>
  );
}

export default Course;
