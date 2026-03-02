![License](https://img.shields.io/badge/license-MIT-blue)
![Backend](https://img.shields.io/badge/backend-FastAPI-009688)
![Frontend](https://img.shields.io/badge/frontend-React-61DAFB)
![Database](https://img.shields.io/badge/database-SQLite-003B57)
![Auth](https://img.shields.io/badge/auth-JWT%20%2B%20bcrypt-green)

# HealthOS

FastAPI + React health platform — medical records, lab results, medications on one timeline. Plugin architecture for extensibility.

## Why

My health data lives in six different patient portals. Each one has its own login, its own format, its own idea of what "recent" means. None of them talk to each other.

HealthOS puts medical records, lab results, and medications on one timeline. Same place, same format, one login.

The part I actually care about architecturally: each health domain is a plugin. Labs, medications, medical records — they all implement the same `BaseModule` abstract class, register at startup via the module registry, and expose standard methods for timeline events, data import/export, and cross-module queries. The base class includes `query_related_module()` so any module can reach into any other through the registry — the plumbing for things like medications checking lab results before surfacing interaction warnings. Adding a new domain means implementing one abstract class, not rewiring the app.

The auth layer does the small things that matter: rate-limited login (5/min via slowapi), a password reset endpoint that always returns "email sent" whether the account exists or not (anti-enumeration), and JWT tokens with bcrypt hashing.

Your health data shouldn't require six browser tabs to understand.

## Architecture

```
┌─────────────────────────────────────┐
│          React Frontend              │
│    Timeline · Records · Labs · Meds  │
└───────────────┬─────────────────────┘
                │ REST API
                ▼
┌─────────────────────────────────────┐
│          FastAPI Gateway             │
│  Auth (JWT) · CORS · Rate Limiting   │
│         Pydantic Validation          │
└───────────────┬─────────────────────┘
                │
       ┌────────┼────────┬────────┐
       ▼        ▼        ▼        ▼
┌──────────┐ ┌───────┐ ┌──────┐ ┌────────────┐
│ Medical  │ │ Labs  │ │ Meds │ │ [Your      │
│ Records  │ │       │ │      │ │  Module]   │
│ Module   │ │Module │ │Module│ │            │
└─────┬────┘ └───┬───┘ └──┬───┘ └─────┬──────┘
      │          │        │            │
      └──────────┼────────┼────────────┘
                 │ BaseModule interface
                 ▼
┌─────────────────────────────────────┐
│       Timeline Service               │
│  Aggregates events from all modules  │
└───────────────┬─────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│      SQLite (SQLAlchemy ORM)         │
└─────────────────────────────────────┘
```

## Plugin Architecture

Each health domain implements `BaseModule`:

```python
class BaseModule(ABC):
    # Identity
    name: str                    # "medications"
    display_name: str            # "Medications"
    description: str             # Human-readable
    version: str                 # Semver

    # Data access
    has_data(user_id) -> bool
    get_data_summary(user_id) -> dict
    get_last_update(user_id) -> datetime | None

    # I/O
    import_data(user_id, file_path, file_type) -> dict
    export_data(user_id, format) -> bytes

    # Timeline integration
    get_timeline_events(user_id, start_date, end_date) -> list[dict]

    # Cross-module queries
    query_related_module(module_name, query) -> Any | None
    execute_query(query) -> Any

    # Optional
    dependencies: list[str]      # Modules this one requires
    enhances: list[str]          # Modules this one extends
    get_insights(user_id) -> list[dict]
    get_correlations(user_id, other_module) -> dict | None
```

Modules register via `ModuleRegistry` at startup. The registry syncs module metadata to the database and provides discovery (`is_module_available`, `get_module`, `list_modules`).

The Timeline Service queries all registered modules for events within a date range and merges them chronologically.

**Adding a new domain** (imaging, vitals, allergies):
1. Create a class implementing `BaseModule`
2. Register it — timeline and cross-module queries work automatically

## Screenshots

<!-- To be added -->

## Features

- **3 health modules** — medical records, lab results, medications (extensible via BaseModule)
- **Unified timeline** — chronological view aggregated from all modules
- **JWT authentication** — bcrypt hashing, rate limiting (slowapi), anti-enumeration on password reset
- **Module registry** — auto-discovery, DB-synced metadata, cross-module query infrastructure
- **Data import** — file-based import endpoint for health data
- **Docker deployment** — `docker-compose up` for the full stack

## Quick Start

### Docker (recommended)

```bash
docker-compose up
# Backend on :8000, frontend on :5173
```

### Manual

```bash
# Backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Change HEALTHOS_SECRET_KEY
uvicorn app.main:app --reload
# → http://localhost:8000 (docs at /docs)

# Frontend
cd frontend
npm install && npm run dev
# → http://localhost:5173
```

### Seed test data

```bash
cd backend && python seed_data.py
# test@healthos.dev / password123
```

## API Endpoints

**Auth**
- `POST /api/auth/register` — rate-limited 5/min
- `POST /api/auth/login` — rate-limited 5/min
- `POST /api/auth/password-reset-request` — rate-limited 3/hr, anti-enumeration
- `POST /api/auth/password-reset`

**Health Data** (all protected)
- `GET/POST /api/medical-records/`
- `GET/POST /api/labs/`
- `GET/POST /api/medications/`

**Platform**
- `GET /api/timeline/` — unified chronological view
- `GET /api/modules/` — list registered modules
- `POST /api/imports/` — file-based data import

## Environment Variables

| Variable | Default | Notes |
|----------|---------|-------|
| `HEALTHOS_SECRET_KEY` | `change-me` | **Must change in production** |
| `HEALTHOS_DATABASE_URL` | `sqlite:///./data/database/healthos.db` | SQLAlchemy connection string |
| `HEALTHOS_ACCESS_TOKEN_EXPIRE_MINUTES` | `60` | JWT token lifetime |
| `HEALTHOS_LOG_LEVEL` | `INFO` | Python logging level |

## Tests

```bash
cd backend
pytest tests/unit/ -v
pytest tests/integration/ -v
```

Unit tests (auth, health data) + integration tests (module system).

## Known Trade-offs

- **SQLite** — good enough for personal health tracking, not for multi-tenant SaaS
- **No email sending** — password reset logs the token in dev mode, email TODO in production
- **Cross-module queries exist in BaseModule but aren't used yet** — the `query_related_module()` infrastructure is built, individual modules haven't wired up cross-queries
- **No CI/CD** — tests exist but no automated pipeline
- **Import is basic** — file upload endpoint exists, format-specific parsers are minimal

## See Also

- [anti-slop-design](https://github.com/Cuuper22/anti-slop-design) — design skill that generated this project's UI patterns
- [Erdos](https://github.com/Cuuper22/Erdos) — same engineering approach (modular architecture, real tests) applied to theorem proving

## License

MIT
