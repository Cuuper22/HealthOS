# HealthOS

Personal health intelligence platform. Unifies genomic data, medical records, lab results, wearable metrics, and lifestyle data into one locally-hosted system.

This is a personal project, not a product. Built for one user (me), designed to actually be useful rather than impressive on a landing page.

## Status

Phase 1 (Foundation) is complete. Backend API is functional, frontend is scaffolded with Vite + React. Actively developing core modules.

There's a 100KB project plan in this repo that covers phases 1-5 in excruciating detail. The README is not that document.

## What It Does

- Ingests and normalizes health data from multiple sources (genomics, labs, wearables, medical records)
- Stores everything locally in a structured database
- Exposes a REST API for querying and analysis
- React frontend for visualization (in progress)

## Stack

**Backend:**
- Python / FastAPI
- SQLite (local-first, no cloud dependency)
- Modular architecture -- each health domain is its own module

**Frontend:**
- React + TypeScript
- Vite
- Talking to the FastAPI backend

## Running It

### Backend

```bash
cd backend
pip install -r requirements.txt
python -m app.main
```

API runs on `http://localhost:8000`. Docs at `/docs`.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Project Structure

```
HealthOS/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI entry point
│   │   ├── config.py         # Configuration
│   │   ├── database.py       # DB setup
│   │   ├── models/           # Data models
│   │   ├── modules/          # Health domain modules
│   │   ├── services/         # Business logic
│   │   ├── api/              # Route handlers
│   │   └── utils/            # Helpers
│   ├── requirements.txt
│   └── tests/
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
└── README.md
```

## License

Personal project. Not currently accepting contributions.
