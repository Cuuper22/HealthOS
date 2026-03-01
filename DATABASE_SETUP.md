# Database Setup Guide

## Quick Start (SQLite - Default)

The application uses SQLite by default and will automatically create the database on first run.

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The database file will be created at `backend/data/database/healthos.db`.

## Manual Database Initialization

If you need to manually initialize the database:

```python
from app.database import Base, engine
Base.metadata.create_all(bind=engine)
```

Or via the FastAPI app startup event (automatic):

```bash
uvicorn app.main:app
```

## Database Schema

The database includes the following tables:

### users
- `id` (UUID, primary key)
- `email` (string, unique)
- `password_hash` (string)
- `first_name` (string, optional)
- `last_name` (string, optional)
- `date_of_birth` (date, optional)
- `sex` (string, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

### medical_records
- `id` (UUID, primary key)
- `user_id` (UUID, foreign key)
- `encounter_date` (date)
- `provider` (string, optional)
- `diagnosis` (string, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

### lab_results
- `id` (UUID, primary key)
- `user_id` (UUID, foreign key)
- `test_name` (string)
- `result_value` (float)
- `unit` (string, optional)
- `result_date` (date)
- `reference_range` (string, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

### medications
- `id` (UUID, primary key)
- `user_id` (UUID, foreign key)
- `name` (string)
- `dosage` (string, optional)
- `start_date` (date, optional)
- `end_date` (date, optional)
- `status` (string, default: 'active')
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

### timeline_events
- `id` (UUID, primary key)
- `user_id` (UUID, foreign key)
- `event_type` (string)
- `event_date` (datetime)
- `module_name` (string)
- `source_record_id` (UUID, optional)
- `title` (string)
- `description` (text, optional)
- `severity` (string, optional)
- `created_at` (datetime)

### module_registry
- `module_name` (string, primary key)
- `display_name` (string)
- `version` (string, optional)
- `description` (text, optional)
- `is_enabled` (boolean, default: True)
- `registered_at` (datetime)

### data_imports
- `id` (UUID, primary key)
- `user_id` (UUID, foreign key)
- `source` (string)
- `status` (string)
- `records_imported` (integer)
- `errors` (text, optional)
- `imported_at` (datetime)

### audit_logs
- `id` (UUID, primary key)
- `user_id` (UUID, foreign key, optional)
- `action` (string)
- `resource_type` (string)
- `resource_id` (UUID, optional)
- `details` (text, optional)
- `created_at` (datetime)

## Using PostgreSQL (Production)

1. Create a PostgreSQL database:
```bash
createdb healthos
```

2. Set the database URL in your `.env` file:
```bash
HEALTHOS_DATABASE_URL=postgresql://username:password@localhost/healthos
```

3. Install PostgreSQL driver:
```bash
pip install psycopg2-binary
```

4. Run the application (tables will be created automatically):
```bash
uvicorn app.main:app
```

## Resetting the Database

**WARNING: This will delete all data!**

### SQLite
```bash
rm backend/data/database/healthos.db
```

### PostgreSQL
```bash
dropdb healthos
createdb healthos
```

Then restart the application to recreate tables.

## Backup and Restore

### SQLite Backup
```bash
cp backend/data/database/healthos.db backend/data/database/healthos_backup_$(date +%Y%m%d).db
```

### PostgreSQL Backup
```bash
pg_dump healthos > healthos_backup_$(date +%Y%m%d).sql
```

### PostgreSQL Restore
```bash
psql healthos < healthos_backup_20260228.sql
```

## Migrations (Future)

For production deployments, consider using Alembic for database migrations:

```bash
pip install alembic
alembic init alembic
# Configure alembic.ini and env.py
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```
