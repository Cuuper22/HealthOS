import type { FormEvent } from 'react';
import { useState } from 'react';

import { createMedication } from '../services/api';

const Medications = () => {
  const [userId, setUserId] = useState('');
  const [name, setName] = useState('');
  const [dosage, setDosage] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [statusValue, setStatusValue] = useState('active');
  const [notes, setNotes] = useState('');
  const [status, setStatus] = useState('');

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    setStatus('Saving...');
    try {
      await createMedication({
        user_id: userId,
        name,
        dosage,
        start_date: startDate || undefined,
        end_date: endDate || undefined,
        status: statusValue,
        notes,
      });
      setStatus('Saved medication.');
    } catch (error) {
      setStatus('Unable to save medication.');
    }
  };

  return (
    <section className="card">
      <h1>Medications</h1>
      <p>Track active and past medications with dosing details.</p>
      <form className="form" onSubmit={handleSubmit}>
        <label>
          User ID
          <input value={userId} onChange={(event) => setUserId(event.target.value)} required />
        </label>
        <label>
          Medication name
          <input value={name} onChange={(event) => setName(event.target.value)} required />
        </label>
        <label>
          Dosage
          <input value={dosage} onChange={(event) => setDosage(event.target.value)} />
        </label>
        <label>
          Start date
          <input type="date" value={startDate} onChange={(event) => setStartDate(event.target.value)} />
        </label>
        <label>
          End date
          <input type="date" value={endDate} onChange={(event) => setEndDate(event.target.value)} />
        </label>
        <label>
          Status
          <select value={statusValue} onChange={(event) => setStatusValue(event.target.value)}>
            <option value="active">Active</option>
            <option value="paused">Paused</option>
            <option value="completed">Completed</option>
          </select>
        </label>
        <label>
          Notes
          <textarea value={notes} onChange={(event) => setNotes(event.target.value)} />
        </label>
        <button type="submit">Save Medication</button>
      </form>
      {status ? <p className="status">{status}</p> : null}
    </section>
  );
};

export default Medications;
