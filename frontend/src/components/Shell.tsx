import { PropsWithChildren } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

const Shell = ({ children }: PropsWithChildren) => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className="shell">
      <header className="shell__header">
        <div className="shell__brand">HealthOS</div>
        <nav className="shell__nav">
          {user ? (
            <>
              <Link to="/">Dashboard</Link>
              <Link to="/timeline">Timeline</Link>
              <Link to="/medical-records">Medical Records</Link>
              <Link to="/labs">Labs</Link>
              <Link to="/medications">Medications</Link>
              <span style={{ marginLeft: 'auto', color: '#666' }}>
                {user.first_name || user.email}
              </span>
              <button
                onClick={handleLogout}
                style={{
                  background: 'none',
                  border: '1px solid #ccc',
                  padding: '0.5rem 1rem',
                  cursor: 'pointer',
                }}
              >
                Logout
              </button>
            </>
          ) : (
            <>
              <Link to="/login">Login</Link>
              <Link to="/register">Register</Link>
            </>
          )}
        </nav>
      </header>
      <main className="shell__content">{children}</main>
    </div>
  );
};

export default Shell;
