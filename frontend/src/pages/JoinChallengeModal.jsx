import { Dialog, DialogContent, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { useState } from "react";

export default function JoinChallengeModal({ open, setOpen, challengeId, onJoined }) {
  const [loading, setLoading] = useState(false);

  const handleConfirm = async () => {
    setLoading(true);
    try {
      const access = localStorage.getItem('access');
      const res = await fetch(`http://127.0.0.1:8000/api/challenges/${challengeId}/join/`, {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${access}`,
          'Content-Type': 'application/json',
        },
      });

      const data = await res.json();
      if (res.ok) {
        onJoined();
        setOpen(false);
      } else {
        alert(data.detail || 'Ошибка при вступлении');
      }
    } catch {
      alert('Сетевая ошибка');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Присоединиться к челленджу?</DialogTitle>
        </DialogHeader>
        <div className="flex justify-end gap-2 mt-4">
          <Button variant="outline" onClick={() => setOpen(false)}>
            Отмена
          </Button>
          <Button onClick={handleConfirm} disabled={loading}>
            {loading ? 'Присоединение...' : 'Присоединиться'}
          </Button>
        </div>
      </DialogContent>
    </Dialog>
  );
}
