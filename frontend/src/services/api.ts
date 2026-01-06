const API_BASE = import.meta.env.VITE_API_URL ?? 'http://localhost:8000';

export type ModuleStatus = {
  module_name: string;
  display_name: string;
  description: string | null;
  version: string | null;
  is_enabled: boolean;
  has_data: boolean;
  last_data_update: string | null;
};

export type TimelineEvent = {
  id: string;
  user_id: string;
  event_type: string;
  event_date: string;
  module_name: string;
  title: string;
  description?: string | null;
  severity?: string | null;
};

const handleResponse = async <T>(response: Response): Promise<T> => {
  if (!response.ok) {
    throw new Error('Request failed');
  }
  return response.json() as Promise<T>;
};

export const fetchModules = () =>
  fetch(`${API_BASE}/api/modules/`).then((response) => handleResponse<ModuleStatus[]>(response));

export const fetchTimeline = (userId: string) =>
  fetch(`${API_BASE}/api/timeline/?user_id=${userId}`).then((response) =>
    handleResponse<TimelineEvent[]>(response),
  );

export const createMedicalRecord = (payload: {
  user_id: string;
  encounter_date: string;
  provider?: string;
  diagnosis?: string;
  notes?: string;
}) =>
  fetch(`${API_BASE}/api/medical-records/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  }).then((response) => handleResponse(response));

export const createLabResult = (payload: {
  user_id: string;
  test_name: string;
  result_value: number;
  unit?: string;
  result_date: string;
  reference_range?: string;
  notes?: string;
}) =>
  fetch(`${API_BASE}/api/labs/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  }).then((response) => handleResponse(response));

export const createMedication = (payload: {
  user_id: string;
  name: string;
  dosage?: string;
  start_date?: string;
  end_date?: string;
  status?: string;
  notes?: string;
}) =>
  fetch(`${API_BASE}/api/medications/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  }).then((response) => handleResponse(response));
