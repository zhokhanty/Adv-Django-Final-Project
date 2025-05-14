import { useState } from 'react';
import JoinChallengeModal from '../pages/JoinChallengeModal';

export default function ChallengeCard({ challenge }) {
  const [joined, setJoined] = useState(false);
  const [modalOpen, setModalOpen] = useState(false);

  return (
    <div className="challenge-card">
      <h3>{challenge.title}</h3>
      <p>{challenge.description}</p>
      {!joined && (
        <Button onClick={() => setModalOpen(true)}>Join Challenge</Button>
      )}
      {joined && <p className="joined-message">✅ Вы участвуете</p>}

      <JoinChallengeModal
        open={modalOpen}
        setOpen={setModalOpen}
        challengeId={challenge.id}
        onJoined={() => setJoined(true)}
      />
    </div>
  );
}
