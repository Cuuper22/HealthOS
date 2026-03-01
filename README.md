# HealthOS

A FastAPI + React health platform for tracking medical records, lab results, medications, and health timeline.

## Features

- JWT-based authentication (register/login)
- Medical records tracking
- Laboratory results management
- Medication tracking  
- Unified health timeline
- Modular architecture
- Full test coverage

## Setup

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

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
