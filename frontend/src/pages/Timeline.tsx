import { useState } from 'react';

import { fetchTimeline, TimelineEvent } from '../services/api';

const Timeline = () => {
  const [userId, setUserId] = useState('');
  const [events, setEvents] = useState<TimelineEvent[]>([]);
  const [status, setStatus] = useState('');

  const handleLoad = async () => {
    setStatus('Loading...');
    try {
      const data = await fetchTimeline(userId);
      setEvents(data);
      setStatus(data.length ? '' : 'No events yet.');
    } catch (error) {
      setStatus('Unable to load timeline.');
    }
  };

  return (
    <section className="card">
      <h1>Timeline</h1>
      <p>Unified view of health events from all modules.</p>
      <div className="form form--inline">
        <label>
          User ID
          <input value={userId} onChange={(event) => setUserId(event.target.value)} />
        </label>
        <button type="button" onClick={handleLoad}>
          Load Timeline
        </button>
      </div>
      {status ? <p className="status">{status}</p> : null}
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
    </section>
  );
};

export default Timeline;
