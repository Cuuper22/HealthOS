import type { FormEvent } from 'react';
import { useState } from 'react';

import { createLabResult } from '../services/api';

const Labs = () => {
  const [userId, setUserId] = useState('');
  const [testName, setTestName] = useState('');
  const [resultValue, setResultValue] = useState('');
  const [unit, setUnit] = useState('');
  const [resultDate, setResultDate] = useState('');
  const [referenceRange, setReferenceRange] = useState('');
  const [notes, setNotes] = useState('');
  const [status, setStatus] = useState('');

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    setStatus('Saving...');
    try {
      await createLabResult({
        user_id: userId,
        test_name: testName,
        result_value: Number(resultValue),
        unit,
        result_date: resultDate,
        reference_range: referenceRange,
        notes,
      });
      setStatus('Saved lab result.');
    } catch (error) {
      setStatus('Unable to save lab result.');
    }
  };

  return (
    <section className="card">
      <h1>Laboratory Results</h1>
      <p>Track lab results and reference ranges.</p>
      <form className="form" onSubmit={handleSubmit}>
        <label>
          User ID
          <input value={userId} onChange={(event) => setUserId(event.target.value)} required />
        </label>
        <label>
          Test name
          <input value={testName} onChange={(event) => setTestName(event.target.value)} required />
        </label>
        <label>
          Result value
          <input
            type="number"
            step="0.01"
            value={resultValue}
            onChange={(event) => setResultValue(event.target.value)}
            required
          />
        </label>
        <label>
          Unit
          <input value={unit} onChange={(event) => setUnit(event.target.value)} />
        </label>
        <label>
          Result date
          <input
            type="date"
            value={resultDate}
            onChange={(event) => setResultDate(event.target.value)}
            required
          />
        </label>
        <label>
          Reference range
          <input
            value={referenceRange}
            onChange={(event) => setReferenceRange(event.target.value)}
          />
        </label>
        <label>
          Notes
          <textarea value={notes} onChange={(event) => setNotes(event.target.value)} />
        </label>
        <button type="submit">Save Lab Result</button>
      </form>
      {status ? <p className="status">{status}</p> : null}
    </section>
  );
};

export default Labs;
