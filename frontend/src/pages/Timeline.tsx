import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

import { fetchTimeline, TimelineEvent } from '../services/api';
import { useAuth } from '../contexts/AuthContext';

const Timeline = () => {
  const [events, setEvents] = useState<TimelineEvent[]>([]);
  const [status, setStatus] = useState('');
  const [isLoading, setIsLoading] = useState(true);
  const { user } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (!user) {
      navigate('/login');
      return;
    }

    const loadTimeline = async () => {
      setStatus('Loading...');
      setIsLoading(true);
      try {
        const data = await fetchTimeline();
        setEvents(data);
        setStatus(data.length ? '' : 'No events yet.');
      } catch (error) {
        setStatus('Unable to load timeline. ' + (error instanceof Error ? error.message : ''));
      } finally {
        setIsLoading(false);
      }
    };

    loadTimeline();
  }, [user, navigate]);

  if (!user) {
    return null;
  }

  return (
    <section className="card">
      <h1>Timeline</h1>
      <p>Unified view of health events from all modules.</p>
      {status ? <p className="status">{status}</p> : null}
      {isLoading ? (
        <p>Loading timeline...</p>
      ) : (
        <ul className="timeline">
          {events.map((event) => (
            <li key={event.id} className="timeline__item">
              <div>
                <strong>{event.title}</strong>
                <span className="timeline__meta">{new Date(event.event_date).toLocaleDateString()}</span>
              </div>
              <p>{event.description}</p>
              <span className="tag">{event.module_name}</span>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
};

export default Timeline;
