import type { FormEvent } from 'react';
import { useState } from 'react';

import { createMedicalRecord } from '../services/api';

const MedicalRecords = () => {
  const [userId, setUserId] = useState('');
  const [encounterDate, setEncounterDate] = useState('');
  const [provider, setProvider] = useState('');
  const [diagnosis, setDiagnosis] = useState('');
  const [notes, setNotes] = useState('');
  const [status, setStatus] = useState('');

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    setStatus('Saving...');
    try {
      await createMedicalRecord({
        user_id: userId,
        encounter_date: encounterDate,
        provider,
        diagnosis,
        notes,
      });
      setStatus('Saved medical record.');
    } catch (error) {
      setStatus('Unable to save record.');
    }
  };

  return (
    <section className="card">
      <h1>Medical Records</h1>
      <p>Capture clinical encounters and diagnoses.</p>
      <form className="form" onSubmit={handleSubmit}>
        <label>
          User ID
          <input value={userId} onChange={(event) => setUserId(event.target.value)} required />
        </label>
        <label>
          Encounter date
          <input
            type="date"
            value={encounterDate}
            onChange={(event) => setEncounterDate(event.target.value)}
            required
          />
        </label>
        <label>
          Provider
          <input value={provider} onChange={(event) => setProvider(event.target.value)} />
        </label>
        <label>
          Diagnosis
          <input value={diagnosis} onChange={(event) => setDiagnosis(event.target.value)} />
        </label>
        <label>
          Notes
          <textarea value={notes} onChange={(event) => setNotes(event.target.value)} />
        </label>
        <button type="submit">Save Record</button>
      </form>
      {status ? <p className="status">{status}</p> : null}
    </section>
  );
};

export default MedicalRecords;
