import { PropsWithChildren } from 'react';
import { Link } from 'react-router-dom';

const Shell = ({ children }: PropsWithChildren) => {
  return (
    <div className="shell">
      <header className="shell__header">
        <div className="shell__brand">HealthOS</div>
        <nav className="shell__nav">
          <Link to="/">Dashboard</Link>
          <Link to="/timeline">Timeline</Link>
          <Link to="/medical-records">Medical Records</Link>
          <Link to="/labs">Labs</Link>
          <Link to="/medications">Medications</Link>
          <Link to="/login">Login</Link>
          <Link to="/register">Register</Link>
        </nav>
      </header>
      <main className="shell__content">{children}</main>
    </div>
  );
};

export default Shell;
