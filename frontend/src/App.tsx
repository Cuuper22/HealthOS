import { Route, Routes } from 'react-router-dom';

import Dashboard from './pages/Dashboard';
import Labs from './pages/Labs';
import Login from './pages/Login';
import MedicalRecords from './pages/MedicalRecords';
import Medications from './pages/Medications';
import Register from './pages/Register';
import Timeline from './pages/Timeline';
import Shell from './components/Shell';
import ErrorBoundary from './components/ErrorBoundary';
import { AuthProvider } from './contexts/AuthContext';

const App = () => {
  return (
    <ErrorBoundary>
      <AuthProvider>
        <Shell>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/timeline" element={<Timeline />} />
            <Route path="/medical-records" element={<MedicalRecords />} />
            <Route path="/labs" element={<Labs />} />
            <Route path="/medications" element={<Medications />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
          </Routes>
        </Shell>
      </AuthProvider>
    </ErrorBoundary>
  );
};

export default App;
