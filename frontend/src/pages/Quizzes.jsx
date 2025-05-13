import React from 'react';
import { useState, useEffect } from 'react';
import QuizCard from '../components/QuizCard';

export default function QuizzesPage({ lessonId }) {
  const [quizzes, setQuizzes] = useState([]);

  useEffect(() => {
    fetch(`http://localhost:8000/api/lesson/${lessonId}/quizzes/`)
      .then(res => res.json())
      .then(data => setQuizzes(data));
  }, [lessonId]);

  return (
    <div>
      <h1>Quizzes</h1>
      {quizzes.map(quiz => (
        <QuizCard 
          key={quiz.id}
          question={quiz.question}
          options={quiz.options}
          correct_option={quiz.correct_option}
        />
      ))}
    </div>
  );
}