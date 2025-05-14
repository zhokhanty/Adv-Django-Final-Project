import React, { useState, useEffect } from 'react';
import { useAuth } from '../AuthPage/AuthContext';
import './Challenge.css';

export default function MyChallengesPage() {
  const [myChallenges, setMyChallenges] = useState([]);
  const [filterCompleted, setFilterCompleted] = useState(null);
  const [loading, setLoading] = useState(true);
  const { isAuthenticated } = useAuth();

  useEffect(() => {
    if (!isAuthenticated) return;

    const fetchMyChallenges = async () => {
      try {
        let url = '/api/my-challenges/';
        if (filterCompleted !== null) {
          url += `?completed=${filterCompleted}`;
        }

        const response = await fetch(url, {
          headers: {
            'Authorization': `Token ${localStorage.getItem('token')}`,
          },
        });
        const data = await response.json();
        setMyChallenges(data);
      } catch (error) {
        console.error('Error fetching my challenges:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchMyChallenges();
  }, [isAuthenticated, filterCompleted]);

  const handleCompleteDay = async (progressId) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/challenge-progress/${progressId}/`, {
        method: 'POST',
        headers: {
          'Authorization': `Token ${localStorage.getItem('token')}`,
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        alert('Day marked as completed!');
        const updatedResponse = await fetch('/api/my-challenges/', {
          headers: {
            'Authorization': `Token ${localStorage.getItem('token')}`,
          },
        });
        setMyChallenges(await updatedResponse.json());
      } else {
        const errorData = await response.json();
        alert(errorData.detail || 'Failed to complete day');
      }
    } catch (error) {
      console.error('Error completing day:', error);
    }
  };

  if (!isAuthenticated) return <div>Please login to view your challenges</div>;
  if (loading) return <div>Loading your challenges...</div>;

  return (
    <div className="my-challenges-container">
      <h1>My Challenges</h1>
      
      <div className="filter-controls">
        <button 
          onClick={() => setFilterCompleted(null)}
          className={filterCompleted === null ? 'active' : ''}
        >
          All
        </button>
        <button 
          onClick={() => setFilterCompleted('true')}
          className={filterCompleted === 'true' ? 'active' : ''}
        >
          Completed
        </button>
        <button 
          onClick={() => setFilterCompleted('false')}
          className={filterCompleted === 'false' ? 'active' : ''}
        >
          Active
        </button>
      </div>

      <div className="challenges-list">
        {myChallenges.length === 0 ? (
          <p>You don't have any challenges yet. Join some!</p>
        ) : (
          myChallenges.map(progress => (
            <div key={progress.id} className="challenge-progress-card">
              <h2>{progress.challenge.title}</h2>
              <p>{progress.challenge.description}</p>
              
              <div className="progress-info">
                <div className="progress-bar">
                  <div 
                    className="progress-fill"
                    style={{
                      width: `${(progress.completed_days.length / progress.challenge.duration_days) * 100}%`
                    }}
                  >
                    {progress.completed_days.length}/{progress.challenge.duration_days} days
                  </div>
                </div>
                
                {!progress.completed_at && (
                  <button
                    onClick={() => handleCompleteDay(progress.id)}
                    className="complete-day-btn"
                    disabled={progress.completed_days.includes(new Date().toISOString().split('T')[0])}
                  >
                    Complete Today
                  </button>
                )}
                
                {progress.completed_at && (
                  <div className="completion-badge">
                    Completed on {new Date(progress.completed_at).toLocaleDateString()}
                  </div>
                )}
              </div>
              
              <div className="completed-days">
                <h4>Completed Days:</h4>
                <ul>
                  {progress.completed_days.map((day, index) => (
                    <li key={index}>{new Date(day).toLocaleDateString()}</li>
                  ))}
                </ul>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}