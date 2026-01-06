import { useEffect, useState } from 'react';

import { fetchModules, ModuleStatus } from '../services/api';

const Dashboard = () => {
  const [modules, setModules] = useState<ModuleStatus[]>([]);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchModules()
      .then(setModules)
      .catch(() => setError('Unable to load modules. Is the backend running?'));
  }, []);

  return (
    <section className="card">
      <h1>Welcome to HealthOS</h1>
      <p>Your personal health operating system is ready for setup.</p>
      <div className="card__section">
        <h2>Phase 1 Checklist</h2>
        <ul>
          <li>Register or log in to start your profile.</li>
          <li>Core modules are registered and ready.</li>
          <li>Timeline events unify all health data.</li>
        </ul>
      </div>
      <div className="card__section">
        <h2>Registered Modules</h2>
        {error ? <p className="error">{error}</p> : null}
        <div className="module-grid">
          {modules.map((module) => (
            <div key={module.module_name} className="module-card">
              <h3>{module.display_name}</h3>
              <p>{module.description ?? 'No description available.'}</p>
              <span className={`tag ${module.has_data ? 'tag--active' : ''}`}>
                {module.has_data ? 'Data available' : 'No data yet'}
              </span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Dashboard;
