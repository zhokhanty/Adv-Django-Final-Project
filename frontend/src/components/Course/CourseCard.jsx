import React from 'react';
import { Link } from 'react-router-dom';
import './CourseCard.css';

export default function CourseCard({ 
  courseId,
  title, 
  description, 
  creator, 
  duration_minutes, 
  tags, 
  created_at 
}) {
  const formattedDate = new Date(created_at).toLocaleDateString('ru-RU', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric'
  });

  return (
    <div className="course-card">
      <div className="course-header">
        <h3 className="course-title">{title}</h3>
        <p className="course-description">{description}</p>
      </div>
      
      <div className="course-meta">
        <div className="meta-item">
          <span className="meta-label">Created by:</span>
          <span className="meta-value">{creator?.username || 'Unknown'}</span>
        </div>
        <div className="meta-item">
          <span className="meta-label">Duration:</span>
          <span className="meta-value">{duration_minutes} minutes</span>
        </div>
        {tags.length > 0 && (
          <div className="meta-item">
            <span className="meta-label">Tags:</span>
            <div className="tags-container">
              {tags.map((tag, index) => (
                <span key={index} className="tag">{tag}</span>
              ))}
            </div>
          </div>
        )}
        <div className="meta-item">
          <span className="meta-label">Created at:</span>
          <span className="meta-value">{formattedDate}</span>
        </div>
      </div>

      <div className="course-actions">
        <Link to={`/courses/${courseId}/lessons`} className="action-btn primary">
          Начать обучение
        </Link>
      </div>
    </div>
  );
}