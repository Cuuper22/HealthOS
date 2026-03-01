import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

import { fetchModules, ModuleStatus } from '../services/api';
import { useAuth } from '../contexts/AuthContext';

const Dashboard = () => {
  const [modules, setModules] = useState<ModuleStatus[]>([]);
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(true);
  const { user } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (!user) {
      navigate('/login');
      return;
    }

    setIsLoading(true);
    fetchModules()
      .then(setModules)
      .catch(() => setError('Unable to load modules. Is the backend running?'))
      .finally(() => setIsLoading(false));
  }, [user, navigate]);

  if (!user) {
    return null;
  }

  return (
    <section className="card">
      <h1>Welcome to HealthOS, {user.first_name || user.email}!</h1>
      <p>Your personal health operating system is ready.</p>
      <div className="card__section">
        <h2>Quick Actions</h2>
        <ul>
          <li>
            <a href="/timeline">View your health timeline</a>
          </li>
          <li>
            <a href="/medical-records">Add a medical record</a>
          </li>
          <li>
            <a href="/labs">Record lab results</a>
          </li>
          <li>
            <a href="/medications">Track medications</a>
          </li>
        </ul>
      </div>
      <div className="card__section">
        <h2>Registered Modules</h2>
        {error ? <p className="error">{error}</p> : null}
        {isLoading ? (
          <p>Loading modules...</p>
        ) : (
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
        )}
      </div>
    </section>
  );
};

export default Dashboard;
