import React, { useState, useEffect } from 'react';
import { useAuth } from '../AuthPage/AuthContext';
import JoinChallengeModal from '../JoinChallengeModal';
import './Challenge.css';

export default function ChallengesPage() {
  const [challenges, setChallenges] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedChallengeId, setSelectedChallengeId] = useState(null);
  const [modalOpen, setModalOpen] = useState(false);
  const { isAuthenticated } = useAuth();

  useEffect(() => {
    const fetchChallenges = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/challenges/');
        const data = await response.json();
        setChallenges(data);
      } catch {
        console.error('Ошибка загрузки');
      } finally {
        setLoading(false);
      }
    };

    fetchChallenges();
  }, []);

  const handleOpenModal = (challengeId) => {
    setSelectedChallengeId(challengeId);
    setModalOpen(true);
  };

  const handleJoined = () => {
    setChallenges(prev =>
      prev.map(c =>
        c.id === selectedChallengeId ? { ...c, joined: true } : c
      )
    );
  };

  if (loading) return <div>Loading challenges...</div>;

  return (
    <div className="challenges-container">
      <h1>Available Challenges</h1>
      <div className="challenges-grid">
        {challenges.map(challenge => (
          <div key={challenge.id} className="challenge-card">
            <h2>{challenge.title}</h2>
            <p>{challenge.description}</p>
            <div className="challenge-meta">
              <span>Duration: {challenge.duration_days} days</span>
              <span>Starts: {new Date(challenge.start_date).toLocaleDateString()}</span>
              <span>Ends: {new Date(challenge.end_date).toLocaleDateString()}</span>
            </div>
            {isAuthenticated && !challenge.joined && (
              <button 
                onClick={() => handleOpenModal(challenge.id)}
                className="join-btn"
              >
                Join Challenge
              </button>
            )}
            {challenge.joined && <span className="joined-label">You joined</span>}
          </div>
        ))}
      </div>

      {selectedChallengeId && (
        <JoinChallengeModal
          open={modalOpen}
          setOpen={setModalOpen}
          challengeId={selectedChallengeId}
          onJoined={handleJoined}
        />
      )}
    </div>
  );
}
