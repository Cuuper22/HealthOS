## Why

My health data lives in six different patient portals. Each one has its own login, its own format, its own idea of what "recent" means. None of them talk to each other.

HealthOS puts medical records, lab results, and medications on one timeline. Same place, same format, one login.

The part I actually care about architecturally: each health domain is a plugin. Labs, medications, medical records — they all implement the same `BaseModule` interface, register themselves at startup, and expose standard methods for timeline events, data import/export, and cross-module queries. The medications module can check if lab results exist before surfacing interaction warnings. Adding a new domain means implementing one abstract class, not rewiring the app.

The auth layer does the small things that matter: rate-limited login, a password reset endpoint that always returns "email sent" whether the account exists or not (anti-enumeration), and an audit log that captures before/after values on every write.

Your health data shouldn't require six browser tabs to understand.

# HealthOS

A production-ready FastAPI + React health platform for tracking medical records, lab results, medications, and unified health timeline.

## Features

- **Authentication**: JWT-based auth with bcrypt password hashing, rate limiting, and password reset
- **Medical Records**: Track doctor visits, diagnoses, and notes
- **Lab Results**: Record and view laboratory test results with reference ranges
- **Medications**: Manage current and past medications with dosage validation
- **Timeline**: Unified chronological view of all health events
- **Security**: CORS protection, input validation, auth middleware
- **Production Ready**: Error boundaries, loading states, pagination, consistent API errors

## Quick Start with Docker

```bash
docker-compose up
```

This will start both backend (port 8000) and frontend (port 5173).

## Manual Setup

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and configure:
```bash
cp .env.example .env
# Edit .env and change HEALTHOS_SECRET_KEY to a secure random value
```

5. Run the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

API docs: `http://localhost:8000/docs`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm run dev
```

Frontend will be available at `http://localhost:5173`

## Development Workflow

### Create Test Data

Run the seed script to create a test user and sample data:

```bash
cd backend
python seed_data.py
```

Test credentials:
- Email: `test@healthos.dev`
- Password: `password123`

### Database Setup

See [DATABASE_SETUP.md](./DATABASE_SETUP.md) for detailed database configuration, migrations, and backup instructions.

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login and get JWT token

### Medical Records (Protected)
- `GET /api/medical-records/` - List user's medical records
- `POST /api/medical-records/` - Create medical record

### Lab Results (Protected)
- `GET /api/labs/` - List user's lab results
- `POST /api/labs/` - Create lab result

### Medications (Protected)
- `GET /api/medications/` - List user's medications
- `POST /api/medications/` - Create medication

### Timeline (Protected)
- `GET /api/timeline/` - Get unified health timeline

### Modules
- `GET /api/modules/` - List available modules

### Data Import (Protected)
- `POST /api/imports/` - Import health data from file

## Authentication

Protected endpoints require a JWT token in the Authorization header:

```
Authorization: Bearer <token>
```

Get a token by registering or logging in.

## Running Tests

```bash
cd backend
pytest tests/unit/ -v
pytest tests/integration/ -v
```

## Architecture

- **FastAPI backend** with SQLAlchemy ORM
- **SQLite database** (configurable via `HEALTHOS_DATABASE_URL`)
- **JWT authentication** with bcrypt password hashing
- **Modular system** for extending functionality
- **Timeline service** for unified health events

## Environment Variables

- `HEALTHOS_DATABASE_URL` - Database connection string (default: sqlite:///./data/database/healthos.db)
- `HEALTHOS_SECRET_KEY` - JWT signing key (default: change-me, MUST change in production)
- `HEALTHOS_ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiration (default: 60)
- `HEALTHOS_LOG_LEVEL` - Logging level (default: INFO)

## Development

The codebase follows these principles:

- Type hints throughout
- Dependency injection for auth
- Session-based database access
- Comprehensive test coverage
- Clear separation of concerns (routes, services, models)

## Security

- Passwords hashed with bcrypt
- JWT tokens for stateless authentication
- User data isolation (enforced at query level)
- Protected endpoints via dependency injection

## License

MIT
