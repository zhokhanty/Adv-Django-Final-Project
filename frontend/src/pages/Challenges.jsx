import React from 'react';
import { useState, useEffect } from 'react';
import ChallengeCard from '../components/ChallengeCard';

export default function ChallengesPage() {
  const [challenges, setChallenges] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/challenges/')
      .then(res => res.json())
      .then(data => setChallenges(data));
  }, []);

  return (
    <div>
      <h1>Challenges</h1>
      {challenges.map(challenge => (
        <ChallengeCard 
          key={challenge.id}
          title={challenge.title}
          description={challenge.description}
          days={challenge.days}
          tags={challenge.tags}
          created_at={challenge.created_at}
        />
      ))}
    </div>
  );
}