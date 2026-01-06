# Personal Health OS - Comprehensive Project Plan

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Project Phases Overview](#project-phases-overview)
3. [Phase 1: Foundation](#phase-1-foundation)
4. [Phase 2: Core Modules](#phase-2-core-modules)
5. [Phase 3: Advanced Features](#phase-3-advanced-features)
6. [Phase 4: Intelligence & Analytics](#phase-4-intelligence--analytics)
7. [Phase 5: Polish & Deploy](#phase-5-polish--deploy)
8. [Technical Specifications](#technical-specifications)
9. [Testing Strategy](#testing-strategy)
10. [Deployment Strategy](#deployment-strategy)
11. [Risk Mitigation](#risk-mitigation)
12. [Success Milestones](#success-milestones)

---

## Executive Summary

Personal Health OS is a comprehensive, locally-hosted personal health intelligence system that unifies genomic data, medical records, laboratory results, wearable metrics, lifestyle data, and environmental factors into a single adaptive platform.

### Core Design Principles

1. **Adaptive Architecture**: Every module works independently; the system never breaks due to missing data
2. **Graceful Degradation**: Features scale based on available data sources
3. **Progressive Enhancement**: Start with basic functionality, add sophistication as data accumulates
4. **Privacy-First**: 100% local data storage, no cloud dependencies for core functionality

### Technology Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.11+, Flask/FastAPI |
| Database | SQLite with SQLCipher encryption |
| Frontend | React 18+, Material-UI/Tailwind CSS |
| Data Analysis | Pandas, NumPy, SciPy, Scikit-learn |
| Visualization | Recharts/Chart.js |
| PDF Generation | ReportLab/WeasyPrint |
| Optional AI | Claude API (anthropic-sdk-python) |

### Module Categories

| Tier | Modules | Purpose |
|------|---------|---------|
| Tier 1: Core | Timeline, Medical Records, Labs, Medications | Foundation functionality |
| Tier 2: Clinical | Genomics, Family History, Immunizations, Imaging, Procedures | Advanced clinical data |
| Tier 3: Lifestyle | Wearables, Sleep, Activity, Nutrition, Weight, CGM | Continuous health metrics |
| Tier 4: Subjective | Symptoms, Mental Health, Menstrual Cycle, Environmental | Personal tracking |
| Tier 5: Specialized | Microbiome, Hormones, Supplements, Epigenetics | Deep health analysis |
| Tier 6: Support | Voice Notes, Research, Emergency Info | Auxiliary functions |

---

## Project Phases Overview

The project is divided into five major phases, each building upon the previous while maintaining the core principle of **adaptive functionality** - the system works at every stage, even with minimal data.

### Phase Summary

```
Phase 1: Foundation          ████████░░░░░░░░░░░░  (~20% of effort)
Phase 2: Core Modules         ████████████░░░░░░░░  (~30% of effort)
Phase 3: Advanced Features    ██████████░░░░░░░░░░  (~25% of effort)
Phase 4: Intelligence         ██████░░░░░░░░░░░░░░  (~15% of effort)
Phase 5: Polish & Deploy      ████░░░░░░░░░░░░░░░░  (~10% of effort)
```

### Phase 1: Foundation
**Goal**: Establish project infrastructure, database architecture, and core framework

**Key Deliverables**:
- Project structure with modular architecture
- SQLite database with encryption (SQLCipher)
- Base module system with graceful degradation
- React frontend skeleton with routing
- Authentication and user profile system
- Basic API framework

**Success Criteria**: Empty application runs, user can log in, modules can be registered

---

### Phase 2: Core Modules
**Goal**: Implement Tier 1 modules that form the backbone of the system

**Key Deliverables**:
- Timeline & Events module (universal health event logging)
- Medical Records module (clinical encounters, diagnoses)
- Laboratory Results module (test tracking, trends)
- Medications module (current/past medications, interactions)
- Data import system (PDF parsing, manual entry, CSV)
- Basic visualization components

**Success Criteria**: User can import and view medical records, labs, and medications with basic timeline

---

### Phase 3: Advanced Features
**Goal**: Implement Tier 2-4 modules and cross-module functionality

**Key Deliverables**:
- Genomics module (VCF parsing, variant annotation)
- Wearables module (Apple Health, Fitbit import)
- Sleep and Activity tracking
- Symptoms and Mental Health logging
- Family History module
- Cross-module correlation basics
- Provider report generation (PDF/FHIR)

**Success Criteria**: All major data sources can be imported; basic correlations work

---

### Phase 4: Intelligence & Analytics
**Goal**: Implement advanced analysis, AI insights, and comprehensive correlations

**Key Deliverables**:
- Multi-module correlation engine
- Statistical analysis with significance testing
- AI-powered insights (optional Claude API integration)
- Pharmacogenomic analysis
- Risk stratification algorithms
- Advanced visualization (heatmaps, multi-axis charts)
- Predictive trend analysis

**Success Criteria**: System identifies meaningful health patterns; AI provides actionable insights

---

### Phase 5: Polish & Deploy
**Goal**: Production-ready application with full documentation

**Key Deliverables**:
- Desktop application packaging (Electron)
- Installation wizard
- Complete user documentation
- Performance optimization
- Security audit and hardening
- Backup/restore system
- Mobile-responsive interface finalization

**Success Criteria**: Non-technical user can install and use application independently

---

### Module Implementation Order

The modules are implemented in a specific order to maximize value delivery while respecting dependencies:

```
Implementation Order:

1. Timeline & Events        [FOUNDATION - Required for all other modules]
       ↓
2. User Profile & Settings  [FOUNDATION - Authentication, preferences]
       ↓
3. Medical Records          [TIER 1 - Core clinical data]
       ↓
4. Laboratory Results       [TIER 1 - Critical health metrics]
       ↓
5. Medications              [TIER 1 - Drug tracking, basic interactions]
       ↓
6. Wearables/Vitals         [TIER 3 - High user value, continuous data]
       ↓
7. Sleep Tracking           [TIER 3 - Builds on wearables]
       ↓
8. Physical Activity        [TIER 3 - Builds on wearables]
       ↓
9. Symptoms Diary           [TIER 4 - Enables correlations]
       ↓
10. Genomics                [TIER 2 - Complex but high value]
       ↓
11. Family History          [TIER 2 - Enhances genomic risk]
       ↓
12. Nutrition               [TIER 3 - Enables metabolic correlations]
       ↓
13. Weight & Body Comp      [TIER 3 - Links nutrition/activity]
       ↓
14. Mental Health & Mood    [TIER 4 - Correlation target]
       ↓
15. Remaining Tier 2-5      [In order of user demand]
       ↓
16. Provider Reports        [Depends on multiple modules]
       ↓
17. AI Insights Engine      [Requires all data sources]
```

### Rationale for Implementation Order

| Priority | Module | Rationale |
|----------|--------|-----------|
| 1 | Timeline | Backbone for all health events; required infrastructure |
| 2 | User Profile | Security and personalization foundation |
| 3 | Medical Records | Most universally needed; establishes clinical context |
| 4 | Labs | Objective health data; enables trend tracking |
| 5 | Medications | Safety-critical; enables drug interaction checking |
| 6-8 | Wearables/Sleep/Activity | High engagement; continuous data; wearables are popular |
| 9 | Symptoms | Enables correlation analysis with objective data |
| 10-11 | Genomics/Family History | Complex but differentiating; requires parsing infrastructure |
| 12-14 | Nutrition/Weight/Mood | Lifestyle factors that correlate with clinical data |
| 15+ | Remaining | Based on user demand and development capacity |

---

## Phase 1: Foundation

### Overview
Phase 1 establishes the technical foundation for the entire system. Every subsequent phase depends on the infrastructure built here. The key principle is to create an **extensible module system** that supports graceful degradation from day one.

### 1.1 Project Setup

#### Backend Development Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 1.1.1 | Initialize Python project | Create project with Poetry/pip, set up virtual environment | None |
| 1.1.2 | Configure project structure | Set up directory structure following clean architecture | 1.1.1 |
| 1.1.3 | Install core dependencies | Flask/FastAPI, SQLAlchemy, Pandas, etc. | 1.1.1 |
| 1.1.4 | Configure linting/formatting | Set up Black, isort, flake8, mypy | 1.1.1 |
| 1.1.5 | Create configuration system | Environment-based config, secrets management | 1.1.2 |
| 1.1.6 | Set up logging framework | Structured logging with rotation | 1.1.2 |

**Project Directory Structure:**
```
healthos/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # Application entry point
│   │   ├── config.py               # Configuration management
│   │   ├── database.py             # Database connection/session
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── routes/             # API route definitions
│   │   │   └── middleware/         # Auth, logging, error handling
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── base.py             # Base SQLAlchemy model
│   │   │   └── user.py             # User model
│   │   ├── modules/
│   │   │   ├── __init__.py
│   │   │   ├── base.py             # Base module class
│   │   │   ├── registry.py         # Module registration system
│   │   │   └── [module_name]/      # Individual modules
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── analysis/           # Data analysis services
│   │   │   ├── import/             # Data import services
│   │   │   └── export/             # Data export services
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── parsing.py          # File parsing utilities
│   │       └── validation.py       # Data validation
│   ├── tests/
│   │   ├── unit/
│   │   ├── integration/
│   │   └── fixtures/
│   ├── migrations/                  # Alembic migrations
│   ├── pyproject.toml
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── store/
│   │   └── utils/
│   ├── public/
│   └── package.json
├── data/                            # Local data storage
│   ├── database/
│   └── uploads/
├── docs/
└── docker-compose.yml               # Optional containerization
```

#### Frontend Development Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 1.1.7 | Initialize React project | Create React app with Vite or CRA | None |
| 1.1.8 | Configure TypeScript | Set up strict TypeScript configuration | 1.1.7 |
| 1.1.9 | Install UI framework | Set up Material-UI or Tailwind CSS | 1.1.7 |
| 1.1.10 | Configure routing | Set up React Router with route structure | 1.1.7 |
| 1.1.11 | Set up state management | Configure Context API or Redux | 1.1.7 |
| 1.1.12 | Create API client | Axios/fetch wrapper with error handling | 1.1.7 |
| 1.1.13 | Configure build system | Production build optimization | 1.1.7 |

---

### 1.2 Database Architecture

#### Database Development Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 1.2.1 | Set up SQLite with SQLCipher | Configure encrypted database | 1.1.2 |
| 1.2.2 | Create base model classes | Timestamped base, soft delete, audit fields | 1.2.1 |
| 1.2.3 | Design user schema | User profile, authentication, preferences | 1.2.2 |
| 1.2.4 | Design module registry schema | Track available modules, their status | 1.2.2 |
| 1.2.5 | Create timeline events schema | Universal health event table | 1.2.2 |
| 1.2.6 | Set up Alembic migrations | Database version control | 1.2.1 |
| 1.2.7 | Implement database encryption key management | Secure key storage, rotation | 1.2.1 |

**Core Database Schema (Phase 1):**

```sql
-- Users table
CREATE TABLE users (
    id TEXT PRIMARY KEY,
    email TEXT UNIQUE,
    password_hash TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    date_of_birth DATE,
    sex TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    settings JSON DEFAULT '{}'
);

-- Module registry
CREATE TABLE module_registry (
    id TEXT PRIMARY KEY,
    module_name TEXT UNIQUE NOT NULL,
    display_name TEXT NOT NULL,
    description TEXT,
    version TEXT,
    is_enabled BOOLEAN DEFAULT TRUE,
    has_data BOOLEAN DEFAULT FALSE,
    last_data_update TIMESTAMP,
    settings JSON DEFAULT '{}',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Universal timeline events (backbone of all modules)
CREATE TABLE timeline_events (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    event_type TEXT NOT NULL,           -- 'lab_result', 'medication', 'symptom', etc.
    event_date TIMESTAMP NOT NULL,
    module_name TEXT NOT NULL,          -- Source module
    source_record_id TEXT,              -- ID in source module's table
    title TEXT NOT NULL,
    description TEXT,
    severity TEXT,                      -- 'info', 'warning', 'critical'
    metadata JSON DEFAULT '{}',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_timeline_user_date (user_id, event_date),
    INDEX idx_timeline_module (module_name)
);

-- Audit log
CREATE TABLE audit_log (
    id TEXT PRIMARY KEY,
    user_id TEXT REFERENCES users(id),
    action TEXT NOT NULL,               -- 'create', 'read', 'update', 'delete'
    table_name TEXT NOT NULL,
    record_id TEXT,
    old_values JSON,
    new_values JSON,
    ip_address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Data imports tracking
CREATE TABLE data_imports (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    module_name TEXT NOT NULL,
    file_name TEXT,
    file_type TEXT,
    status TEXT DEFAULT 'pending',      -- 'pending', 'processing', 'completed', 'failed'
    records_imported INTEGER DEFAULT 0,
    records_failed INTEGER DEFAULT 0,
    error_message TEXT,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 1.3 Module System Architecture

#### Module Framework Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 1.3.1 | Design base module interface | Abstract class defining module contract | 1.2.2 |
| 1.3.2 | Implement module registry | Dynamic module discovery and registration | 1.3.1, 1.2.4 |
| 1.3.3 | Create module status API | Check if module has data, last update, etc. | 1.3.2 |
| 1.3.4 | Implement graceful degradation | Modules handle missing dependencies gracefully | 1.3.2 |
| 1.3.5 | Create module communication interface | Cross-module queries with null safety | 1.3.2 |
| 1.3.6 | Build module settings system | Per-module configuration storage | 1.3.2 |

**Base Module Interface (Python):**

```python
from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any
from datetime import datetime

class BaseModule(ABC):
    """
    Abstract base class for all HealthOS modules.

    Every module must implement these methods to ensure
    consistent behavior and graceful degradation.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique module identifier (e.g., 'laboratory_results')"""
        pass

    @property
    @abstractmethod
    def display_name(self) -> str:
        """Human-readable name (e.g., 'Laboratory Results')"""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Module description for UI"""
        pass

    @property
    @abstractmethod
    def version(self) -> str:
        """Module version (semver)"""
        pass

    @property
    def dependencies(self) -> List[str]:
        """List of module names this module depends on (optional)"""
        return []

    @property
    def enhances(self) -> List[str]:
        """List of modules this module enhances when both present"""
        return []

    # Status methods
    @abstractmethod
    def has_data(self, user_id: str) -> bool:
        """Check if user has any data in this module"""
        pass

    @abstractmethod
    def get_data_summary(self, user_id: str) -> Dict[str, Any]:
        """Return summary statistics for module data"""
        pass

    @abstractmethod
    def get_last_update(self, user_id: str) -> Optional[datetime]:
        """Return timestamp of most recent data"""
        pass

    # Data operations
    @abstractmethod
    def import_data(self, user_id: str, file_path: str,
                    file_type: str) -> Dict[str, Any]:
        """Import data from file, return import results"""
        pass

    @abstractmethod
    def export_data(self, user_id: str, format: str) -> bytes:
        """Export module data in specified format"""
        pass

    # Timeline integration
    @abstractmethod
    def get_timeline_events(self, user_id: str,
                           start_date: datetime,
                           end_date: datetime) -> List[Dict[str, Any]]:
        """Return events for unified timeline"""
        pass

    # Cross-module queries (graceful degradation)
    def query_related_module(self, module_name: str,
                            query: Dict[str, Any]) -> Optional[Any]:
        """
        Query another module for related data.
        Returns None if module unavailable or has no data.
        """
        from app.modules.registry import ModuleRegistry
        registry = ModuleRegistry()

        if not registry.is_module_available(module_name):
            return None

        module = registry.get_module(module_name)
        if not module.has_data(query.get('user_id')):
            return None

        return module.execute_query(query)

    def execute_query(self, query: Dict[str, Any]) -> Any:
        """Execute a cross-module query (override in subclass)"""
        raise NotImplementedError("Module does not support cross-queries")

    # Analysis (optional, override for module-specific analysis)
    def get_insights(self, user_id: str) -> List[Dict[str, Any]]:
        """Generate module-specific insights"""
        return []

    def get_correlations(self, user_id: str,
                        other_module: str) -> Optional[Dict[str, Any]]:
        """Calculate correlations with another module's data"""
        return None

    # Schema
    @abstractmethod
    def get_database_models(self) -> List[Any]:
        """Return SQLAlchemy models for this module"""
        pass
```

---

### 1.4 API Framework

#### API Development Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 1.4.1 | Create API router structure | Organize routes by module | 1.1.3 |
| 1.4.2 | Implement authentication middleware | JWT-based authentication | 1.4.1 |
| 1.4.3 | Create error handling middleware | Consistent error responses | 1.4.1 |
| 1.4.4 | Implement request validation | Pydantic/Marshmallow schemas | 1.4.1 |
| 1.4.5 | Create OpenAPI documentation | Auto-generated API docs | 1.4.1 |
| 1.4.6 | Implement rate limiting | Prevent abuse (optional for local) | 1.4.1 |
| 1.4.7 | Create CORS configuration | Allow frontend communication | 1.4.1 |

**Core API Endpoints (Phase 1):**

```
Authentication:
  POST   /api/auth/register          - Create new user
  POST   /api/auth/login             - Authenticate user
  POST   /api/auth/logout            - End session
  POST   /api/auth/refresh           - Refresh JWT token
  GET    /api/auth/me                - Get current user

User:
  GET    /api/user/profile           - Get user profile
  PUT    /api/user/profile           - Update user profile
  PUT    /api/user/password          - Change password
  GET    /api/user/settings          - Get user settings
  PUT    /api/user/settings          - Update settings

Modules:
  GET    /api/modules                - List all modules with status
  GET    /api/modules/{name}         - Get module details
  GET    /api/modules/{name}/status  - Check if module has data
  PUT    /api/modules/{name}/enable  - Enable/disable module
  GET    /api/modules/{name}/settings - Get module settings
  PUT    /api/modules/{name}/settings - Update module settings

Timeline:
  GET    /api/timeline               - Get unified timeline events
  GET    /api/timeline/search        - Search timeline
  POST   /api/timeline/events        - Add manual event

Data Management:
  POST   /api/import                 - Upload file for import
  GET    /api/import/{id}/status     - Check import status
  GET    /api/export                 - Export all data
  GET    /api/export/{module}        - Export single module

System:
  GET    /api/health                 - Health check
  GET    /api/version                - Get app version
```

---

### 1.5 Authentication & Security

#### Security Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 1.5.1 | Implement password hashing | bcrypt/argon2 password storage | 1.2.3 |
| 1.5.2 | Create JWT token system | Access and refresh tokens | 1.4.2 |
| 1.5.3 | Implement session management | Track active sessions | 1.5.2 |
| 1.5.4 | Add biometric unlock support | Optional fingerprint/face ID (desktop) | 1.5.2 |
| 1.5.5 | Create audit logging | Track all data access | 1.2.2 |
| 1.5.6 | Implement data encryption utilities | Encrypt sensitive fields | 1.2.7 |
| 1.5.7 | Set up HTTPS configuration | TLS for network mode | 1.4.1 |

---

### 1.6 Frontend Foundation

#### Frontend Core Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 1.6.1 | Create layout components | Header, sidebar, main content area | 1.1.9 |
| 1.6.2 | Build navigation system | Dynamic nav based on enabled modules | 1.1.10, 1.6.1 |
| 1.6.3 | Implement authentication UI | Login, register, password reset | 1.6.1 |
| 1.6.4 | Create dashboard skeleton | Home page with module status cards | 1.6.2 |
| 1.6.5 | Build settings page | User profile, preferences, module config | 1.6.2 |
| 1.6.6 | Create reusable components | Buttons, forms, modals, alerts | 1.1.9 |
| 1.6.7 | Implement loading states | Skeletons, spinners, progress bars | 1.6.6 |
| 1.6.8 | Create error boundaries | Graceful error handling | 1.6.6 |
| 1.6.9 | Build file upload component | Drag-and-drop with progress | 1.6.6 |
| 1.6.10 | Implement responsive design | Mobile-first responsive layouts | 1.6.1 |

**Key Frontend Components (Phase 1):**

```
src/
├── components/
│   ├── common/
│   │   ├── Button/
│   │   ├── Card/
│   │   ├── Modal/
│   │   ├── Form/
│   │   ├── Table/
│   │   ├── Loading/
│   │   ├── Alert/
│   │   └── FileUpload/
│   ├── layout/
│   │   ├── Header/
│   │   ├── Sidebar/
│   │   ├── MainContent/
│   │   └── Footer/
│   └── modules/
│       └── ModuleStatusCard/
├── pages/
│   ├── Login/
│   ├── Register/
│   ├── Dashboard/
│   ├── Settings/
│   └── NotFound/
├── hooks/
│   ├── useAuth.ts
│   ├── useApi.ts
│   ├── useModules.ts
│   └── useLocalStorage.ts
├── services/
│   ├── api.ts
│   ├── auth.ts
│   └── modules.ts
├── store/
│   ├── AuthContext.tsx
│   └── ModuleContext.tsx
└── utils/
    ├── formatters.ts
    ├── validators.ts
    └── constants.ts
```

---

### 1.7 Testing Infrastructure

#### Testing Setup Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 1.7.1 | Configure pytest for backend | Test runner, fixtures, coverage | 1.1.1 |
| 1.7.2 | Set up test database | In-memory SQLite for tests | 1.2.1 |
| 1.7.3 | Create test factories | Generate test data | 1.7.1 |
| 1.7.4 | Configure Jest for frontend | React testing library | 1.1.7 |
| 1.7.5 | Set up E2E testing framework | Playwright or Cypress | 1.1.7 |
| 1.7.6 | Create CI pipeline | GitHub Actions for testing | All above |

---

### Phase 1 Success Criteria

| Criterion | Verification Method |
|-----------|---------------------|
| Application starts without errors | Run `python -m app` and `npm start` |
| User can register and login | Manual test registration flow |
| Module registry shows empty modules | API returns module list with has_data=false |
| Database encryption works | Attempt to open DB without key fails |
| All API endpoints respond | Run API test suite |
| Frontend renders all pages | Navigate through all routes |
| Test suite passes | Run `pytest` and `npm test` |

### Phase 1 Deliverables Checklist

- [ ] Python backend with Flask/FastAPI running
- [ ] SQLite database with encryption
- [ ] User authentication system
- [ ] Module registry framework
- [ ] Base module class with graceful degradation
- [ ] Timeline events table
- [ ] React frontend with routing
- [ ] Login/register UI
- [ ] Dashboard with module status
- [ ] Settings page
- [ ] File upload component
- [ ] API documentation
- [ ] Unit test framework
- [ ] Development environment documentation

---

## Phase 2: Core Modules

### Overview
Phase 2 implements the Tier 1 modules that form the backbone of the health tracking system. These modules work independently but share data through the unified timeline. The focus is on establishing the data import pipeline and basic visualization capabilities.

### 2.1 Timeline & Events Module

The timeline module is the backbone of the entire system, providing a unified view of all health events regardless of source.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 2.1.1 | Create timeline data model | Event types, categories, severity levels | 1.2.5 |
| 2.1.2 | Implement timeline API | CRUD operations, filtering, search | 2.1.1 |
| 2.1.3 | Build manual event entry | Add custom health events | 2.1.2 |
| 2.1.4 | Create timeline UI component | Chronological event list with filtering | 2.1.2 |
| 2.1.5 | Implement event detail view | Expandable event cards with full details | 2.1.4 |
| 2.1.6 | Add date range filtering | Day/week/month/year/custom views | 2.1.4 |
| 2.1.7 | Implement category filtering | Filter by module, event type, severity | 2.1.4 |
| 2.1.8 | Create timeline search | Full-text search across events | 2.1.2 |
| 2.1.9 | Build event aggregation | Group related events, show summaries | 2.1.4 |
| 2.1.10 | Add event linking | Link related events across modules | 2.1.1 |

**Timeline Event Schema:**

```python
class TimelineEvent(BaseModel):
    __tablename__ = 'timeline_events'

    id: str = Field(primary_key=True)
    user_id: str = Field(foreign_key='users.id')
    event_type: str  # 'lab_result', 'medication_start', 'symptom', etc.
    event_date: datetime
    module_name: str  # Source module
    source_record_id: Optional[str]  # ID in source module
    title: str
    description: Optional[str]
    severity: str = 'info'  # 'info', 'warning', 'critical'
    category: str  # 'clinical', 'lifestyle', 'medication', etc.
    tags: List[str] = []
    metadata: Dict[str, Any] = {}
    is_manually_entered: bool = False
    created_at: datetime
    updated_at: datetime
```

---

### 2.2 Medical Records Module

Stores and organizes all clinical encounters including visit notes, diagnoses, and procedures.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 2.2.1 | Design medical records schema | Encounters, diagnoses, procedures, providers | 1.2.2 |
| 2.2.2 | Implement ICD-10 code lookup | Diagnosis code validation and descriptions | 2.2.1 |
| 2.2.3 | Implement CPT code lookup | Procedure code validation | 2.2.1 |
| 2.2.4 | Create provider registry | Track healthcare providers | 2.2.1 |
| 2.2.5 | Build PDF parser for clinical docs | Extract structured data from visit notes | 2.2.1 |
| 2.2.6 | Implement FHIR import | Parse FHIR bundles for clinical data | 2.2.1 |
| 2.2.7 | Implement CCD/CDA import | Parse Consolidated CDA documents | 2.2.1 |
| 2.2.8 | Create manual entry forms | Add encounters, diagnoses manually | 2.2.1 |
| 2.2.9 | Build medical records API | CRUD operations, search, filtering | 2.2.1 |
| 2.2.10 | Create records list UI | Sortable, filterable encounters list | 2.2.9 |
| 2.2.11 | Build encounter detail view | Full visit information display | 2.2.10 |
| 2.2.12 | Create diagnosis history view | Timeline of all diagnoses | 2.2.10 |
| 2.2.13 | Implement timeline integration | Push encounter events to timeline | 2.1.1, 2.2.9 |
| 2.2.14 | Add document attachment | Link PDF/images to encounters | 2.2.1 |

**Medical Records Schema:**

```sql
-- Clinical encounters
CREATE TABLE clinical_encounters (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    encounter_date DATE NOT NULL,
    encounter_type TEXT,                -- 'office_visit', 'hospital', 'telehealth', etc.
    provider_id TEXT REFERENCES providers(id),
    facility_name TEXT,
    chief_complaint TEXT,
    notes TEXT,
    summary TEXT,                       -- AI-generated or manual summary
    source_file TEXT,                   -- Original PDF if imported
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Diagnoses (linked to encounters)
CREATE TABLE diagnoses (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    encounter_id TEXT REFERENCES clinical_encounters(id),
    icd10_code TEXT,
    description TEXT NOT NULL,
    diagnosis_date DATE NOT NULL,
    status TEXT DEFAULT 'active',       -- 'active', 'resolved', 'chronic'
    is_primary BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Procedures (linked to encounters)
CREATE TABLE procedures (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    encounter_id TEXT REFERENCES clinical_encounters(id),
    cpt_code TEXT,
    description TEXT NOT NULL,
    procedure_date DATE NOT NULL,
    provider_id TEXT REFERENCES providers(id),
    outcome TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Healthcare providers
CREATE TABLE providers (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    name TEXT NOT NULL,
    specialty TEXT,
    npi TEXT,                           -- National Provider Identifier
    phone TEXT,
    address TEXT,
    notes TEXT,
    is_primary_care BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 2.3 Laboratory Results Module

Tracks all laboratory test results with trending and reference range analysis.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 2.3.1 | Design lab results schema | Tests, values, units, reference ranges | 1.2.2 |
| 2.3.2 | Implement LOINC code lookup | Standardized test identification | 2.3.1 |
| 2.3.3 | Build lab PDF parser | Extract results from lab reports | 2.3.1 |
| 2.3.4 | Parse Quest Diagnostics format | Lab-specific parsing rules | 2.3.3 |
| 2.3.5 | Parse LabCorp format | Lab-specific parsing rules | 2.3.3 |
| 2.3.6 | Implement HL7 parser | Parse HL7 lab messages | 2.3.1 |
| 2.3.7 | Create manual entry forms | Add lab results manually | 2.3.1 |
| 2.3.8 | Build lab results API | CRUD, filtering, trend queries | 2.3.1 |
| 2.3.9 | Create results list UI | Table view with out-of-range highlighting | 2.3.8 |
| 2.3.10 | Build trend graphs | Line charts for individual tests | 2.3.8 |
| 2.3.11 | Create panel views | Group related tests (lipid panel, etc.) | 2.3.9 |
| 2.3.12 | Implement reference range analysis | Flag out-of-range values | 2.3.1 |
| 2.3.13 | Add trend detection | Rising/falling/stable indicators | 2.3.8 |
| 2.3.14 | Implement timeline integration | Push lab events to timeline | 2.1.1, 2.3.8 |
| 2.3.15 | Create lab categories | Metabolic, lipid, thyroid, CBC, etc. | 2.3.1 |

**Laboratory Results Schema:**

```sql
-- Lab test results
CREATE TABLE lab_results (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    test_date DATE NOT NULL,
    test_name TEXT NOT NULL,
    loinc_code TEXT,                    -- Standardized test ID
    value REAL,
    value_text TEXT,                    -- For non-numeric results
    unit TEXT,
    reference_range_low REAL,
    reference_range_high REAL,
    reference_range_text TEXT,          -- For complex ranges
    is_abnormal BOOLEAN DEFAULT FALSE,
    abnormal_flag TEXT,                 -- 'high', 'low', 'critical_high', etc.
    category TEXT,                      -- 'metabolic', 'lipid', 'thyroid', etc.
    panel_name TEXT,                    -- 'Basic Metabolic Panel', etc.
    lab_name TEXT,                      -- 'Quest', 'LabCorp', etc.
    ordering_provider TEXT,
    notes TEXT,
    source_file TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_lab_user_date (user_id, test_date),
    INDEX idx_lab_test_name (user_id, test_name)
);

-- Lab test definitions (reference data)
CREATE TABLE lab_test_definitions (
    id TEXT PRIMARY KEY,
    test_name TEXT NOT NULL,
    loinc_code TEXT,
    category TEXT,
    typical_unit TEXT,
    typical_reference_low REAL,
    typical_reference_high REAL,
    description TEXT,
    clinical_significance TEXT
);
```

**Lab Categories and Common Tests:**

| Category | Tests |
|----------|-------|
| Metabolic | Glucose, BUN, Creatinine, eGFR, Sodium, Potassium, CO2, Calcium |
| Lipid | Total Cholesterol, LDL, HDL, Triglycerides, VLDL |
| Liver | AST, ALT, Alkaline Phosphatase, Bilirubin, Albumin, Total Protein |
| Thyroid | TSH, Free T4, Free T3, T3 Uptake |
| CBC | WBC, RBC, Hemoglobin, Hematocrit, Platelets, MCV, MCH, MCHC, RDW |
| Inflammatory | CRP, ESR, Ferritin |
| Vitamins | Vitamin D, Vitamin B12, Folate |
| Hormones | Testosterone, Estradiol, Cortisol, DHEA-S, Insulin |
| Cardiac | Troponin, BNP, Homocysteine |
| Diabetes | HbA1c, Fasting Glucose, Fasting Insulin, HOMA-IR |

---

### 2.4 Medications Module

Complete medication history with interaction checking and adherence tracking.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 2.4.1 | Design medications schema | Current, past, dosing, indications | 1.2.2 |
| 2.4.2 | Implement RxNorm lookup | Drug name standardization | 2.4.1 |
| 2.4.3 | Build drug database integration | OpenFDA or similar for drug info | 2.4.2 |
| 2.4.4 | Implement drug-drug interaction API | Check for interaction warnings | 2.4.3 |
| 2.4.5 | Create medication entry forms | Add/edit medications | 2.4.1 |
| 2.4.6 | Build medications API | CRUD, active/inactive filtering | 2.4.1 |
| 2.4.7 | Create medications list UI | Current and past medications | 2.4.6 |
| 2.4.8 | Build medication detail view | Full medication information | 2.4.7 |
| 2.4.9 | Implement interaction warnings UI | Display interactions on add/view | 2.4.4, 2.4.7 |
| 2.4.10 | Create medication timeline | Gantt-style medication history | 2.4.6 |
| 2.4.11 | Add adherence logging | Track doses taken | 2.4.1 |
| 2.4.12 | Implement reminder system | Medication reminders (optional) | 2.4.11 |
| 2.4.13 | Create side effect logging | Associate symptoms with meds | 2.4.1 |
| 2.4.14 | Implement timeline integration | Push med events to timeline | 2.1.1, 2.4.6 |
| 2.4.15 | Build prescription import | Parse prescription info from PDFs | 2.4.1 |

**Medications Schema:**

```sql
-- Medications
CREATE TABLE medications (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    name TEXT NOT NULL,                  -- Generic or brand name
    generic_name TEXT,
    brand_name TEXT,
    rxnorm_code TEXT,
    dose TEXT,                           -- '10 mg'
    dose_value REAL,
    dose_unit TEXT,
    frequency TEXT,                      -- 'twice daily', 'once daily', etc.
    route TEXT,                          -- 'oral', 'topical', 'injection', etc.
    indication TEXT,                     -- Why prescribed
    prescriber TEXT,
    pharmacy TEXT,
    start_date DATE,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    is_prn BOOLEAN DEFAULT FALSE,        -- As needed
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Medication adherence logs
CREATE TABLE medication_logs (
    id TEXT PRIMARY KEY,
    medication_id TEXT NOT NULL REFERENCES medications(id),
    user_id TEXT NOT NULL REFERENCES users(id),
    taken_at TIMESTAMP NOT NULL,
    dose_taken TEXT,
    skipped BOOLEAN DEFAULT FALSE,
    skip_reason TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Drug interactions (cached from external API)
CREATE TABLE drug_interactions (
    id TEXT PRIMARY KEY,
    drug1_rxnorm TEXT NOT NULL,
    drug2_rxnorm TEXT NOT NULL,
    severity TEXT,                       -- 'minor', 'moderate', 'major', 'contraindicated'
    description TEXT,
    clinical_effects TEXT,
    management TEXT,
    source TEXT,
    last_updated TIMESTAMP,
    UNIQUE(drug1_rxnorm, drug2_rxnorm)
);

-- Medication side effects
CREATE TABLE medication_side_effects (
    id TEXT PRIMARY KEY,
    medication_id TEXT NOT NULL REFERENCES medications(id),
    user_id TEXT NOT NULL REFERENCES users(id),
    symptom TEXT NOT NULL,
    severity TEXT,                       -- 'mild', 'moderate', 'severe'
    onset_date DATE,
    resolution_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 2.5 Data Import System

Universal import pipeline supporting multiple file formats and sources.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 2.5.1 | Create import queue system | Background processing of imports | 1.2.2 |
| 2.5.2 | Build file type detection | Identify PDF, CSV, XML, JSON | 2.5.1 |
| 2.5.3 | Implement PDF text extraction | Extract text from PDF documents | 2.5.2 |
| 2.5.4 | Create PDF table extraction | Extract tabular data from PDFs | 2.5.3 |
| 2.5.5 | Build CSV import parser | Generic CSV handling | 2.5.2 |
| 2.5.6 | Implement FHIR bundle parser | Full FHIR R4 support | 2.5.2 |
| 2.5.7 | Create CCD/CDA parser | Parse Consolidated CDA | 2.5.2 |
| 2.5.8 | Build HL7 v2 parser | Parse HL7 messages | 2.5.2 |
| 2.5.9 | Implement duplicate detection | Prevent duplicate imports | 2.5.1 |
| 2.5.10 | Create import validation | Verify data integrity | 2.5.1 |
| 2.5.11 | Build import review UI | Preview before confirming | 2.5.10 |
| 2.5.12 | Implement partial import | Handle partial failures gracefully | 2.5.1 |
| 2.5.13 | Create import history log | Track all imports | 2.5.1 |
| 2.5.14 | Build import error reporting | Clear error messages with fixes | 2.5.12 |
| 2.5.15 | Implement unit conversion | Handle different units (metric/imperial) | 2.5.1 |

**Import Pipeline Architecture:**

```python
class ImportPipeline:
    """
    Universal import pipeline for all data types.
    Supports graceful failure and partial imports.
    """

    def __init__(self, user_id: str, module_name: str):
        self.user_id = user_id
        self.module_name = module_name
        self.import_id = generate_uuid()

    async def process_file(self, file_path: str) -> ImportResult:
        """Main entry point for file imports."""
        try:
            # 1. Detect file type
            file_type = self.detect_file_type(file_path)

            # 2. Create import record
            import_record = self.create_import_record(file_path, file_type)

            # 3. Parse file based on type
            parser = self.get_parser(file_type)
            parsed_data = await parser.parse(file_path)

            # 4. Validate parsed data
            validated_data, validation_errors = self.validate(parsed_data)

            # 5. Check for duplicates
            unique_data = self.deduplicate(validated_data)

            # 6. Transform to module format
            transformed = self.transform(unique_data)

            # 7. Save to database
            saved_count, save_errors = await self.save(transformed)

            # 8. Update import record
            self.complete_import(import_record, saved_count,
                               len(validation_errors) + len(save_errors))

            return ImportResult(
                success=True,
                import_id=self.import_id,
                records_imported=saved_count,
                records_skipped=len(unique_data) - saved_count,
                errors=validation_errors + save_errors
            )

        except Exception as e:
            self.fail_import(import_record, str(e))
            return ImportResult(success=False, error=str(e))

    def get_parser(self, file_type: str) -> BaseParser:
        """Return appropriate parser for file type."""
        parsers = {
            'pdf': PDFParser,
            'csv': CSVParser,
            'fhir_json': FHIRParser,
            'ccd_xml': CCDParser,
            'hl7': HL7Parser,
            'apple_health_xml': AppleHealthParser,
        }
        return parsers.get(file_type, GenericParser)()
```

---

### 2.6 Basic Visualization Components

Reusable chart components for displaying health data.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 2.6.1 | Set up charting library | Configure Recharts/Chart.js | 1.1.9 |
| 2.6.2 | Create line chart component | Time-series data visualization | 2.6.1 |
| 2.6.3 | Add reference range overlays | Show normal ranges on charts | 2.6.2 |
| 2.6.4 | Create bar chart component | Categorical comparisons | 2.6.1 |
| 2.6.5 | Build data table component | Sortable, filterable tables | 1.6.6 |
| 2.6.6 | Create sparkline component | Mini inline charts | 2.6.1 |
| 2.6.7 | Implement date range selector | Chart zoom and pan | 2.6.2 |
| 2.6.8 | Add chart export | Download as PNG/SVG | 2.6.2 |
| 2.6.9 | Create tooltip component | Hover details on charts | 2.6.2 |
| 2.6.10 | Build responsive chart wrapper | Charts adapt to container size | 2.6.2 |

**Chart Component Interface:**

```typescript
interface HealthChartProps {
  data: DataPoint[];
  xKey: string;           // Key for x-axis values
  yKey: string;           // Key for y-axis values
  referenceRange?: {
    low: number;
    high: number;
  };
  title?: string;
  unit?: string;
  dateRange?: DateRange;
  showTrend?: boolean;
  height?: number;
  onPointClick?: (point: DataPoint) => void;
}

interface DataPoint {
  date: Date;
  value: number;
  label?: string;
  isAbnormal?: boolean;
  metadata?: Record<string, any>;
}
```

---

### Phase 2 Success Criteria

| Criterion | Verification Method |
|-----------|---------------------|
| Can import lab PDF and view results | Import sample lab report, verify data |
| Lab trends display correctly | View 6+ months of same test on chart |
| Can add and view medical encounters | Create encounter, verify timeline |
| Medications show with interactions | Add 2+ meds, check interaction warnings |
| Timeline shows events from all modules | Filter timeline by module |
| Manual entry works for all modules | Add entries without importing |
| Import errors are clearly displayed | Import malformed file, check error message |
| Out-of-range labs are highlighted | Import abnormal value, verify flag |

### Phase 2 Deliverables Checklist

- [ ] Timeline module fully functional
- [ ] Medical records import and display
- [ ] Laboratory results with trends
- [ ] Medications with interaction checking
- [ ] PDF parsing for labs and medical docs
- [ ] FHIR/CCD import capability
- [ ] Manual entry forms for all modules
- [ ] Line charts with reference ranges
- [ ] Data tables with sorting/filtering
- [ ] Import queue with progress tracking
- [ ] Duplicate detection
- [ ] Timeline integration for all modules

---

## Phase 3: Advanced Features

### Overview
Phase 3 implements Tier 2-4 modules including genomics, wearables, and lifestyle tracking. This phase also introduces basic cross-module correlation capabilities and the provider report generation system.

### 3.1 Genomics Module

The most complex module, providing whole genome sequencing analysis and pharmacogenomic insights.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 3.1.1 | Design genomics schema | Variants, annotations, risk scores | 1.2.2 |
| 3.1.2 | Build VCF file parser | Parse standard VCF format | 3.1.1 |
| 3.1.3 | Parse 23andMe raw data | Convert to standard format | 3.1.2 |
| 3.1.4 | Parse AncestryDNA raw data | Convert to standard format | 3.1.2 |
| 3.1.5 | Implement variant storage | Efficient storage for millions of variants | 3.1.1 |
| 3.1.6 | Build ClinVar integration | Fetch pathogenicity data | 3.1.5 |
| 3.1.7 | Implement gnomAD lookup | Population frequency data | 3.1.5 |
| 3.1.8 | Build PharmGKB integration | Pharmacogenomic annotations | 3.1.5 |
| 3.1.9 | Create variant annotation pipeline | Combine multiple sources | 3.1.6, 3.1.7, 3.1.8 |
| 3.1.10 | Implement ACMG classification | Pathogenicity assessment | 3.1.9 |
| 3.1.11 | Build pharmacogenomic profile | Drug metabolism predictions | 3.1.8 |
| 3.1.12 | Create carrier screening | Recessive condition detection | 3.1.9 |
| 3.1.13 | Implement disease risk scoring | Polygenic risk calculations | 3.1.9 |
| 3.1.14 | Build genomics API | Query variants, annotations | 3.1.9 |
| 3.1.15 | Create genomics dashboard UI | Summary view of findings | 3.1.14 |
| 3.1.16 | Build variant browser | Search and filter variants | 3.1.14 |
| 3.1.17 | Create pharmacogenomics view | Drug-gene recommendations | 3.1.11 |
| 3.1.18 | Implement risk report generation | Comprehensive genomic report | 3.1.13 |
| 3.1.19 | Add timeline integration | Key genomic findings to timeline | 2.1.1, 3.1.14 |
| 3.1.20 | Link to medications module | Drug-gene interaction warnings | 2.4.4, 3.1.11 |

**Genomics Schema:**

```sql
-- Genomic variants (potentially millions of records)
CREATE TABLE genomic_variants (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    chromosome TEXT NOT NULL,
    position INTEGER NOT NULL,
    reference_allele TEXT NOT NULL,
    alternate_allele TEXT NOT NULL,
    genotype TEXT,                       -- '0/1', '1/1', etc.
    rs_id TEXT,                          -- dbSNP ID
    gene_symbol TEXT,
    consequence TEXT,                    -- 'missense', 'synonymous', etc.
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_variant_pos (user_id, chromosome, position),
    INDEX idx_variant_gene (user_id, gene_symbol),
    INDEX idx_variant_rs (user_id, rs_id)
);

-- Variant annotations (from external sources)
CREATE TABLE variant_annotations (
    id TEXT PRIMARY KEY,
    variant_id TEXT NOT NULL REFERENCES genomic_variants(id),
    source TEXT NOT NULL,                -- 'clinvar', 'gnomad', 'pharmgkb'
    clinvar_significance TEXT,           -- 'pathogenic', 'benign', etc.
    clinvar_condition TEXT,
    gnomad_frequency REAL,
    pharmgkb_level TEXT,                 -- Evidence level
    pharmgkb_chemicals TEXT,             -- Affected drugs (JSON)
    raw_data JSON,
    last_updated TIMESTAMP,
    UNIQUE(variant_id, source)
);

-- Pharmacogenomic profile (derived)
CREATE TABLE pharmacogenomic_profile (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    gene TEXT NOT NULL,                  -- 'CYP2D6', 'CYP2C19', etc.
    diplotype TEXT,                      -- '*1/*2', etc.
    phenotype TEXT,                      -- 'Poor Metabolizer', 'Normal', etc.
    affected_drugs JSON,                 -- List of drugs affected
    recommendations JSON,                -- Clinical recommendations
    evidence_level TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, gene)
);

-- Disease risk scores (polygenic)
CREATE TABLE disease_risk_scores (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    condition TEXT NOT NULL,
    risk_score REAL,                     -- Percentile or absolute risk
    risk_category TEXT,                  -- 'low', 'average', 'elevated', 'high'
    population_average REAL,
    variant_count INTEGER,               -- Number of variants in score
    confidence TEXT,
    methodology TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, condition)
);
```

**Key Pharmacogenomic Genes:**

| Gene | Drug Class | Impact |
|------|-----------|--------|
| CYP2D6 | Antidepressants, Opioids, Beta-blockers | Metabolism rate |
| CYP2C19 | PPIs, Clopidogrel, Antidepressants | Metabolism rate |
| CYP2C9 | Warfarin, NSAIDs | Metabolism rate |
| CYP3A4 | Statins, Immunosuppressants | Metabolism rate |
| VKORC1 | Warfarin | Sensitivity |
| SLCO1B1 | Statins | Myopathy risk |
| HLA-B*57:01 | Abacavir | Hypersensitivity |
| HLA-B*15:02 | Carbamazepine | Stevens-Johnson risk |
| DPYD | 5-Fluorouracil | Toxicity risk |
| TPMT | Thiopurines | Toxicity risk |

---

### 3.2 Wearables & Continuous Vitals Module

Imports and analyzes data from wearable devices for continuous health monitoring.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 3.2.1 | Design wearables schema | Heart rate, steps, activity, etc. | 1.2.2 |
| 3.2.2 | Build Apple Health XML parser | Parse iOS health export | 3.2.1 |
| 3.2.3 | Build Fitbit API integration | Connect to Fitbit account | 3.2.1 |
| 3.2.4 | Build Garmin Connect integration | Connect to Garmin account | 3.2.1 |
| 3.2.5 | Build Oura Ring integration | Sleep and readiness data | 3.2.1 |
| 3.2.6 | Implement data aggregation | Roll up minute data to daily | 3.2.1 |
| 3.2.7 | Create heart rate analysis | Resting HR, zones, anomalies | 3.2.6 |
| 3.2.8 | Build HRV analysis | Heart rate variability metrics | 3.2.6 |
| 3.2.9 | Create activity scoring | Daily activity classification | 3.2.6 |
| 3.2.10 | Build wearables API | Query metrics by date range | 3.2.6 |
| 3.2.11 | Create vitals dashboard | Overview of all metrics | 3.2.10 |
| 3.2.12 | Build metric detail views | Drill-down for each metric | 3.2.11 |
| 3.2.13 | Create trend analysis | Weekly/monthly trends | 3.2.10 |
| 3.2.14 | Implement anomaly detection | Flag unusual readings | 3.2.6 |
| 3.2.15 | Add timeline integration | Significant vitals to timeline | 2.1.1, 3.2.10 |

**Wearables Schema:**

```sql
-- Raw wearable data (high volume)
CREATE TABLE wearable_data (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    source TEXT NOT NULL,                -- 'apple_health', 'fitbit', etc.
    metric_type TEXT NOT NULL,           -- 'heart_rate', 'steps', 'spo2', etc.
    timestamp TIMESTAMP NOT NULL,
    value REAL NOT NULL,
    unit TEXT,
    metadata JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_wearable_user_type_time (user_id, metric_type, timestamp)
);

-- Daily aggregated metrics
CREATE TABLE daily_metrics (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    date DATE NOT NULL,
    source TEXT,
    -- Heart rate
    resting_heart_rate REAL,
    avg_heart_rate REAL,
    max_heart_rate REAL,
    min_heart_rate REAL,
    -- HRV
    hrv_average REAL,
    hrv_rmssd REAL,
    -- Activity
    steps INTEGER,
    active_calories REAL,
    total_calories REAL,
    distance_km REAL,
    floors_climbed INTEGER,
    active_minutes INTEGER,
    -- Respiratory
    respiratory_rate REAL,
    spo2_average REAL,
    spo2_min REAL,
    -- Other
    body_temperature REAL,
    blood_pressure_systolic REAL,
    blood_pressure_diastolic REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, date)
);
```

---

### 3.3 Sleep Tracking Module

Comprehensive sleep analysis from wearables and manual logging.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 3.3.1 | Design sleep schema | Sessions, stages, quality | 1.2.2 |
| 3.3.2 | Parse Apple Health sleep | Extract sleep data | 3.2.2 |
| 3.3.3 | Parse Fitbit sleep | Extract sleep stages | 3.2.3 |
| 3.3.4 | Parse Oura sleep data | Detailed sleep analysis | 3.2.5 |
| 3.3.5 | Implement manual sleep logging | Manual entry capability | 3.3.1 |
| 3.3.6 | Calculate sleep quality score | Composite quality metric | 3.3.1 |
| 3.3.7 | Analyze sleep consistency | Bedtime/wake time patterns | 3.3.1 |
| 3.3.8 | Build sleep API | Query sleep data | 3.3.1 |
| 3.3.9 | Create sleep dashboard | Overview and trends | 3.3.8 |
| 3.3.10 | Build sleep detail view | Single night analysis | 3.3.9 |
| 3.3.11 | Create sleep stage visualization | Hypnogram display | 3.3.9 |
| 3.3.12 | Implement circadian analysis | Sleep pattern insights | 3.3.7 |
| 3.3.13 | Add timeline integration | Sleep events to timeline | 2.1.1, 3.3.8 |

**Sleep Schema:**

```sql
-- Sleep sessions
CREATE TABLE sleep_sessions (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    date DATE NOT NULL,                  -- Date of sleep (night of)
    bedtime TIMESTAMP,
    wake_time TIMESTAMP,
    time_in_bed_minutes INTEGER,
    total_sleep_minutes INTEGER,
    sleep_efficiency REAL,               -- Percentage
    source TEXT,
    -- Sleep stages (minutes)
    awake_minutes INTEGER,
    light_sleep_minutes INTEGER,
    deep_sleep_minutes INTEGER,
    rem_sleep_minutes INTEGER,
    -- Quality metrics
    sleep_score REAL,                    -- 0-100
    restfulness_score REAL,
    timing_score REAL,
    -- Environmental
    room_temperature REAL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, date)
);

-- Sleep stage timeline (for hypnogram)
CREATE TABLE sleep_stages (
    id TEXT PRIMARY KEY,
    sleep_session_id TEXT NOT NULL REFERENCES sleep_sessions(id),
    stage TEXT NOT NULL,                 -- 'awake', 'light', 'deep', 'rem'
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    duration_minutes INTEGER
);
```

---

### 3.4 Physical Activity Module

Exercise tracking and workout analysis.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 3.4.1 | Design activity schema | Workouts, metrics, goals | 1.2.2 |
| 3.4.2 | Parse Apple Health workouts | Import workout data | 3.2.2 |
| 3.4.3 | Parse Fitbit activities | Import activity data | 3.2.3 |
| 3.4.4 | Parse Garmin activities | Import detailed workout data | 3.2.4 |
| 3.4.5 | Parse Strava exports | Import running/cycling data | 3.4.1 |
| 3.4.6 | Implement manual workout logging | Log workouts manually | 3.4.1 |
| 3.4.7 | Calculate workout metrics | Intensity, effort, etc. | 3.4.1 |
| 3.4.8 | Track training load | Weekly volume and intensity | 3.4.7 |
| 3.4.9 | Build activity API | Query workouts and metrics | 3.4.1 |
| 3.4.10 | Create activity dashboard | Workout summary and trends | 3.4.9 |
| 3.4.11 | Build workout detail view | Single workout analysis | 3.4.10 |
| 3.4.12 | Create activity calendar | Visual workout history | 3.4.10 |
| 3.4.13 | Implement goal tracking | Set and track activity goals | 3.4.9 |
| 3.4.14 | Add timeline integration | Workouts to timeline | 2.1.1, 3.4.9 |

---

### 3.5 Symptoms Diary Module

Track subjective health experiences and identify patterns.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 3.5.1 | Design symptoms schema | Types, severity, attributes | 1.2.2 |
| 3.5.2 | Create symptom entry form | Quick logging interface | 3.5.1 |
| 3.5.3 | Build symptom templates | Common symptom presets | 3.5.2 |
| 3.5.4 | Implement body map UI | Select symptom location | 3.5.2 |
| 3.5.5 | Add trigger tracking | Associate triggers with symptoms | 3.5.1 |
| 3.5.6 | Build symptoms API | CRUD, filtering, patterns | 3.5.1 |
| 3.5.7 | Create symptoms dashboard | Overview and patterns | 3.5.6 |
| 3.5.8 | Build symptom detail view | History of specific symptom | 3.5.7 |
| 3.5.9 | Implement pattern detection | Identify recurring patterns | 3.5.6 |
| 3.5.10 | Create correlation analysis | Link symptoms to other data | 3.5.9 |
| 3.5.11 | Add timeline integration | Symptoms to timeline | 2.1.1, 3.5.6 |
| 3.5.12 | Link to medications | Potential side effects | 2.4.13, 3.5.6 |

**Symptoms Schema:**

```sql
-- Symptom entries
CREATE TABLE symptoms (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    symptom_type TEXT NOT NULL,          -- 'headache', 'fatigue', 'nausea', etc.
    onset_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP,
    severity INTEGER,                    -- 1-10 scale
    location TEXT,                       -- Body location if applicable
    character TEXT,                      -- 'sharp', 'dull', 'throbbing', etc.
    triggers JSON,                       -- Suspected triggers
    relieving_factors JSON,              -- What helped
    associated_symptoms JSON,            -- Other symptoms at same time
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_symptom_user_type (user_id, symptom_type),
    INDEX idx_symptom_time (user_id, onset_time)
);

-- Symptom templates (common patterns)
CREATE TABLE symptom_templates (
    id TEXT PRIMARY KEY,
    user_id TEXT REFERENCES users(id),   -- NULL for system templates
    name TEXT NOT NULL,
    symptom_type TEXT NOT NULL,
    default_attributes JSON,
    is_system BOOLEAN DEFAULT FALSE
);
```

---

### 3.6 Mental Health & Mood Module

Track psychological wellbeing and identify patterns.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 3.6.1 | Design mood schema | Ratings, dimensions, notes | 1.2.2 |
| 3.6.2 | Create daily check-in UI | Quick mood logging | 3.6.1 |
| 3.6.3 | Implement mood dimensions | Mood, energy, stress, anxiety | 3.6.2 |
| 3.6.4 | Add journaling feature | Detailed mood notes | 3.6.1 |
| 3.6.5 | Build mood API | CRUD, trends, patterns | 3.6.1 |
| 3.6.6 | Create mood dashboard | Overview and trends | 3.6.5 |
| 3.6.7 | Build mood calendar | Visual mood history | 3.6.6 |
| 3.6.8 | Implement correlation analysis | Mood vs. sleep, activity, etc. | 3.6.5 |
| 3.6.9 | Add timeline integration | Significant mood events | 2.1.1, 3.6.5 |
| 3.6.10 | Create export for therapy | Sharable mood summary | 3.6.5 |

---

### 3.7 Family History Module

Track genetic and familial disease risk context.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 3.7.1 | Design family history schema | Family tree, conditions | 1.2.2 |
| 3.7.2 | Create family tree UI | Visual family tree builder | 3.7.1 |
| 3.7.3 | Add condition tracking | Medical conditions per family member | 3.7.1 |
| 3.7.4 | Implement age of onset tracking | When conditions developed | 3.7.3 |
| 3.7.5 | Build inheritance analysis | Pattern detection | 3.7.3 |
| 3.7.6 | Build family history API | CRUD, risk analysis | 3.7.1 |
| 3.7.7 | Create family history view | Summary and tree display | 3.7.6 |
| 3.7.8 | Implement risk enhancement | Enhance genomic risk with family data | 3.1.13, 3.7.5 |
| 3.7.9 | Add timeline integration | Family history context | 2.1.1, 3.7.6 |

---

### 3.8 Provider Report Generation

Generate comprehensive reports for healthcare providers.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 3.8.1 | Design report templates | Structure and sections | 2.2, 2.3, 2.4 |
| 3.8.2 | Build PDF report generator | Create formatted PDF reports | 3.8.1 |
| 3.8.3 | Implement FHIR export | Generate FHIR bundles | 3.8.1 |
| 3.8.4 | Create CCD export | Generate CCD/CDA documents | 3.8.1 |
| 3.8.5 | Build report customization UI | Select sections, date range | 3.8.2 |
| 3.8.6 | Create executive summary section | AI-powered or manual summary | 3.8.2 |
| 3.8.7 | Add genomics section | Pharmacogenomics for providers | 3.1.17, 3.8.2 |
| 3.8.8 | Create emergency info card | Wallet card with critical info | 3.8.2 |
| 3.8.9 | Implement report versioning | Track generated reports | 3.8.2 |
| 3.8.10 | Build report preview | View before downloading | 3.8.5 |

**Report Structure:**

```
Provider Report
├── Cover Page
│   ├── Patient Name, DOB, Report Date
│   └── Report Type (Comprehensive, Focused, Emergency)
├── Executive Summary
│   ├── Key Findings
│   ├── Active Conditions
│   └── Current Medications
├── Medical History
│   ├── Diagnoses (with ICD-10)
│   ├── Procedures (with CPT)
│   └── Surgical History
├── Medications
│   ├── Current Medications
│   ├── Past Medications
│   └── Drug-Gene Interactions (if genomics available)
├── Laboratory Results
│   ├── Recent Results
│   ├── Trends (graphs)
│   └── Out-of-Range Summary
├── Genomics (if available)
│   ├── Pharmacogenomic Profile
│   ├── Relevant Pathogenic Variants
│   └── Disclaimer
├── Family History (if available)
├── Wearable Data Summary (if available)
│   ├── Resting Heart Rate Trend
│   ├── Sleep Quality Summary
│   └── Activity Level Summary
├── Appendices
│   ├── Full Lab Results
│   └── Source Documents
└── Footer
    ├── Generated By: Personal Health OS
    ├── Date Generated
    └── Disclaimers
```

---

### 3.9 Basic Correlation System

Implement foundational cross-module correlation capabilities.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 3.9.1 | Design correlation data model | Store computed correlations | 1.2.2 |
| 3.9.2 | Build two-variable correlation | Basic Pearson/Spearman | 3.9.1 |
| 3.9.3 | Implement time-lag analysis | Check lagged correlations | 3.9.2 |
| 3.9.4 | Create correlation API | Query correlations | 3.9.1 |
| 3.9.5 | Build correlation explorer UI | Select and visualize | 3.9.4 |
| 3.9.6 | Implement scatter plot view | Visualize relationships | 3.9.5 |
| 3.9.7 | Add statistical significance | P-values and confidence | 3.9.2 |
| 3.9.8 | Create auto-correlation detection | Find significant patterns | 3.9.7 |
| 3.9.9 | Build insight notifications | Alert on new correlations | 3.9.8 |

---

### Phase 3 Success Criteria

| Criterion | Verification Method |
|-----------|---------------------|
| VCF file imports successfully | Import sample VCF, view variants |
| Pharmacogenomic profile generated | View drug-gene recommendations |
| Apple Health data imports | Import export.xml, view metrics |
| Sleep data displays with stages | View sleep hypnogram |
| Symptoms can be logged quickly | Add symptom in <30 seconds |
| Provider PDF report generates | Create report with all sections |
| FHIR export validates | Validate against FHIR spec |
| Basic correlations work | Find sleep vs. mood correlation |
| Drug-gene interactions show | Add medication with genetic impact |

### Phase 3 Deliverables Checklist

- [ ] Genomics module with VCF parsing
- [ ] Pharmacogenomic profile generation
- [ ] Apple Health import
- [ ] Wearables dashboard with vitals
- [ ] Sleep tracking with stages
- [ ] Activity/workout logging
- [ ] Symptoms diary with patterns
- [ ] Mood/mental health tracking
- [ ] Family history with tree view
- [ ] Provider report PDF generation
- [ ] FHIR and CCD export
- [ ] Basic correlation analysis
- [ ] Cross-module data linking

---

## Phase 4: Intelligence & Analytics

### Overview
Phase 4 focuses on advanced analysis capabilities, AI-powered insights, and sophisticated cross-module intelligence. This phase transforms raw data into actionable health insights.

### 4.1 Advanced Correlation Engine

Build sophisticated multi-variable correlation analysis.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 4.1.1 | Implement multi-variate analysis | 3+ variable correlations | 3.9.2 |
| 4.1.2 | Build confounding variable detection | Identify lurking variables | 4.1.1 |
| 4.1.3 | Create causal inference framework | Distinguish correlation from causation | 4.1.2 |
| 4.1.4 | Implement seasonal adjustment | Account for seasonal patterns | 4.1.1 |
| 4.1.5 | Build dose-response detection | Identify dose-dependent effects | 4.1.1 |
| 4.1.6 | Create pattern recognition engine | Identify complex patterns | 4.1.1 |
| 4.1.7 | Implement anomaly correlation | Link anomalies across modules | 4.1.6 |
| 4.1.8 | Build trigger detection | Identify event triggers | 4.1.6 |
| 4.1.9 | Create intervention analysis | Before/after comparisons | 4.1.1 |
| 4.1.10 | Implement rolling correlations | Track correlation changes over time | 4.1.1 |

**Correlation Engine Architecture:**

```python
class CorrelationEngine:
    """
    Advanced correlation analysis engine supporting
    multi-variate analysis and pattern detection.
    """

    def analyze_pair(self, user_id: str, metric_a: str,
                     metric_b: str, time_range: DateRange) -> CorrelationResult:
        """Basic two-variable correlation with time lag analysis."""
        pass

    def analyze_multivariate(self, user_id: str, metrics: List[str],
                            target: str) -> MultivariateResult:
        """Analyze multiple predictors against a target variable."""
        pass

    def detect_triggers(self, user_id: str, event_type: str,
                       lookback_hours: int = 48) -> List[TriggerCandidate]:
        """Find potential triggers for a specific event type."""
        pass

    def intervention_analysis(self, user_id: str, intervention_date: date,
                             metrics: List[str]) -> InterventionResult:
        """Compare metrics before and after an intervention."""
        pass

    def find_significant_correlations(self, user_id: str,
                                      min_r_squared: float = 0.3,
                                      max_p_value: float = 0.05) -> List[CorrelationResult]:
        """Automatically find all significant correlations."""
        pass
```

---

### 4.2 AI-Powered Insights (Claude API Integration)

Optional integration with Claude API for natural language insights.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 4.2.1 | Design AI integration architecture | Privacy-preserving design | 1.5.6 |
| 4.2.2 | Implement Claude API client | API wrapper with retry logic | 4.2.1 |
| 4.2.3 | Create data summarization prompts | Generate health summaries | 4.2.2 |
| 4.2.4 | Build insight generation system | Create actionable insights | 4.2.3 |
| 4.2.5 | Implement question answering | Answer health data questions | 4.2.2 |
| 4.2.6 | Create report drafting | AI-assisted report writing | 4.2.2 |
| 4.2.7 | Build research correlation | Link data to published studies | 4.2.2 |
| 4.2.8 | Implement privacy controls | User consent and data filtering | 4.2.1 |
| 4.2.9 | Create local AI option | Ollama integration alternative | 4.2.1 |
| 4.2.10 | Build insight review UI | View and manage AI insights | 4.2.4 |

**AI Insights System:**

```python
class AIInsightsEngine:
    """
    AI-powered health insights using Claude API.
    Privacy-first design with user consent controls.
    """

    def __init__(self, api_key: Optional[str] = None,
                 use_local: bool = False):
        self.api_key = api_key
        self.use_local = use_local
        self.enabled_modules: Set[str] = set()

    def generate_summary(self, user_id: str,
                        time_range: DateRange) -> str:
        """Generate natural language summary of health data."""
        if not self.is_enabled():
            return None

        # Collect data from enabled modules only
        data = self._collect_data(user_id, time_range)

        # Generate summary using Claude
        prompt = self._build_summary_prompt(data)
        return self._call_api(prompt)

    def answer_question(self, user_id: str, question: str) -> str:
        """Answer a question about the user's health data."""
        pass

    def generate_insights(self, user_id: str) -> List[Insight]:
        """Generate actionable health insights."""
        pass

    def draft_report_section(self, user_id: str,
                            section: str) -> str:
        """Draft a section of a provider report."""
        pass

    def find_relevant_research(self, user_id: str,
                              topic: str) -> List[ResearchLink]:
        """Find relevant published research for user's data."""
        pass

    def _collect_data(self, user_id: str,
                     time_range: DateRange) -> Dict[str, Any]:
        """Collect data only from user-enabled modules."""
        pass

    def _anonymize_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Remove personally identifiable information."""
        pass
```

**AI Insight Types:**

| Insight Type | Description | Example |
|-------------|-------------|---------|
| Trend Alert | Significant trend detected | "Your HbA1c has risen 0.3% over 6 months" |
| Correlation Discovery | New correlation found | "Sleep under 6hrs correlates with higher next-day glucose" |
| Intervention Suggestion | Actionable recommendation | "Consider discussing statin alternatives due to CYP3A4 variant" |
| Anomaly Explanation | Explain unusual reading | "Yesterday's elevated heart rate likely from increased caffeine" |
| Research Connection | Link to studies | "Your APOE4 status relates to this Alzheimer's prevention study" |

---

### 4.3 Risk Stratification

Comprehensive health risk assessment combining multiple data sources.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 4.3.1 | Design risk scoring framework | Modular risk calculation | 3.1.13, 3.7.5 |
| 4.3.2 | Implement cardiovascular risk | ASCVD, Framingham scores | 4.3.1 |
| 4.3.3 | Build diabetes risk calculator | Prediabetes risk assessment | 4.3.1 |
| 4.3.4 | Create genomic risk integration | Combine PRS with clinical data | 3.1.13, 4.3.1 |
| 4.3.5 | Implement lifestyle risk factors | Add lifestyle modifications | 4.3.1 |
| 4.3.6 | Build risk visualization | Display risk factors and scores | 4.3.1 |
| 4.3.7 | Create risk trend tracking | Monitor risk over time | 4.3.1 |
| 4.3.8 | Implement risk report section | Add to provider reports | 3.8.2, 4.3.1 |
| 4.3.9 | Build intervention recommendations | Suggest risk reduction | 4.3.1 |
| 4.3.10 | Create family history integration | Enhance risk with family data | 3.7.5, 4.3.1 |

**Risk Assessment Framework:**

```python
class RiskAssessmentEngine:
    """
    Comprehensive health risk assessment combining
    multiple data sources with graceful degradation.
    """

    def calculate_cardiovascular_risk(self, user_id: str) -> RiskScore:
        """
        Calculate cardiovascular risk using available data.
        Adapts calculation based on available inputs.
        """
        # Get available data
        labs = self._get_labs(user_id, ['total_cholesterol', 'hdl', 'ldl'])
        vitals = self._get_vitals(user_id, ['blood_pressure', 'bmi'])
        genomics = self._get_genomics(user_id)  # May be None
        family_history = self._get_family_history(user_id)  # May be None

        # Calculate base risk (traditional factors)
        base_score = self._calculate_framingham(labs, vitals)

        # Enhance with genomics if available
        if genomics:
            prs = genomics.get_prs('cardiovascular')
            base_score = self._integrate_prs(base_score, prs)

        # Adjust for family history if available
        if family_history:
            fh_adjustment = self._family_history_adjustment(family_history)
            base_score = self._apply_adjustment(base_score, fh_adjustment)

        return RiskScore(
            score=base_score,
            percentile=self._score_to_percentile(base_score),
            category=self._categorize_risk(base_score),
            data_sources=self._list_data_sources(labs, vitals, genomics, family_history),
            confidence=self._calculate_confidence()
        )
```

---

### 4.4 Predictive Analytics

Predict future health trends based on historical data.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 4.4.1 | Build time-series forecasting | Predict metric trends | 4.1.1 |
| 4.4.2 | Implement lab value prediction | Forecast future lab results | 4.4.1 |
| 4.4.3 | Create weight trajectory | Project weight changes | 4.4.1 |
| 4.4.4 | Build symptom prediction | Predict symptom occurrence | 4.4.1, 4.1.8 |
| 4.4.5 | Implement confidence intervals | Uncertainty quantification | 4.4.1 |
| 4.4.6 | Create what-if scenarios | Model intervention effects | 4.4.1 |
| 4.4.7 | Build prediction visualization | Show forecasts on charts | 4.4.1 |
| 4.4.8 | Implement prediction accuracy tracking | Monitor prediction quality | 4.4.1 |

---

### 4.5 Advanced Visualization

Sophisticated visualization for complex health data.

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 4.5.1 | Build multi-axis charts | Multiple metrics on one chart | 2.6.2 |
| 4.5.2 | Create heatmap visualization | Activity, mood calendars | 2.6.1 |
| 4.5.3 | Implement radar charts | Multi-dimensional health view | 2.6.1 |
| 4.5.4 | Build network visualization | Show relationships between factors | 2.6.1 |
| 4.5.5 | Create interactive dashboards | Customizable layouts | 4.5.1 |
| 4.5.6 | Implement comparison views | Compare time periods | 4.5.1 |
| 4.5.7 | Build annotation system | Add notes to charts | 4.5.1 |
| 4.5.8 | Create exportable visualizations | High-quality image export | 4.5.1 |

---

### Phase 4 Success Criteria

| Criterion | Verification Method |
|-----------|---------------------|
| Multi-variate correlations work | Find 3+ variable relationship |
| AI generates meaningful insights | Review AI summary for accuracy |
| Risk scores calculate correctly | Verify against known calculators |
| Predictions have confidence intervals | View forecast with uncertainty |
| Trigger detection finds patterns | Identify known trigger relationship |
| Visualizations are interactive | Use heatmap, radar charts |
| Privacy controls work | Verify data filtering for AI |

### Phase 4 Deliverables Checklist

- [ ] Multi-variate correlation analysis
- [ ] Trigger detection algorithm
- [ ] Intervention before/after analysis
- [ ] Claude API integration (optional)
- [ ] Natural language health summaries
- [ ] AI-powered insights generation
- [ ] Cardiovascular risk calculator
- [ ] Diabetes risk assessment
- [ ] Genomic risk integration
- [ ] Time-series forecasting
- [ ] Heatmap and radar visualizations
- [ ] Interactive dashboard builder
- [ ] Privacy-preserving AI design

---

## Phase 5: Polish & Deploy

### Overview
Phase 5 focuses on production readiness, packaging, documentation, and deployment. The goal is a polished application that non-technical users can install and use independently.

### 5.1 Desktop Application Packaging

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 5.1.1 | Set up Electron framework | Desktop app shell | All previous phases |
| 5.1.2 | Package Python backend | Bundle with PyInstaller/cx_Freeze | 5.1.1 |
| 5.1.3 | Bundle React frontend | Production build integration | 5.1.1 |
| 5.1.4 | Create Windows installer | NSIS or similar installer | 5.1.2, 5.1.3 |
| 5.1.5 | Create macOS installer | DMG package | 5.1.2, 5.1.3 |
| 5.1.6 | Create Linux packages | AppImage, deb, rpm | 5.1.2, 5.1.3 |
| 5.1.7 | Implement auto-update system | Check and install updates | 5.1.4, 5.1.5, 5.1.6 |
| 5.1.8 | Create portable version | Run without installation | 5.1.2, 5.1.3 |
| 5.1.9 | Optimize startup time | Fast application launch | 5.1.2 |
| 5.1.10 | Implement tray icon | System tray integration | 5.1.1 |

---

### 5.2 Installation & Setup

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 5.2.1 | Create installation wizard | Guided first-time setup | 5.1.4, 5.1.5, 5.1.6 |
| 5.2.2 | Build database initialization | First-run database setup | 5.2.1 |
| 5.2.3 | Create user onboarding flow | Welcome screens and tour | 5.2.1 |
| 5.2.4 | Implement sample data option | Demo with sample health data | 5.2.3 |
| 5.2.5 | Build migration system | Upgrade from previous versions | 5.2.2 |
| 5.2.6 | Create backup/restore wizard | Easy backup management | 5.2.1 |
| 5.2.7 | Implement import wizard | Guide through first import | 5.2.3 |

---

### 5.3 Performance Optimization

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 5.3.1 | Profile database queries | Identify slow queries | All modules |
| 5.3.2 | Implement query caching | Cache frequent queries | 5.3.1 |
| 5.3.3 | Optimize large dataset handling | Efficient pagination | 5.3.1 |
| 5.3.4 | Implement lazy loading | Load data on demand | 5.3.3 |
| 5.3.5 | Optimize frontend bundle | Code splitting, tree shaking | 5.1.3 |
| 5.3.6 | Implement background processing | Offload heavy computations | 5.3.1 |
| 5.3.7 | Create performance monitoring | Track response times | 5.3.1 |
| 5.3.8 | Optimize memory usage | Reduce memory footprint | 5.3.1 |

---

### 5.4 Security Hardening

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 5.4.1 | Conduct security audit | Review code for vulnerabilities | All modules |
| 5.4.2 | Implement input sanitization | Prevent injection attacks | 5.4.1 |
| 5.4.3 | Harden API endpoints | Rate limiting, validation | 5.4.1 |
| 5.4.4 | Review encryption implementation | Verify encryption strength | 5.4.1 |
| 5.4.5 | Implement secure update channel | Signed updates | 5.1.7 |
| 5.4.6 | Create security documentation | Security best practices | 5.4.1 |
| 5.4.7 | Implement session security | Token rotation, timeout | 5.4.1 |

---

### 5.5 Documentation

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 5.5.1 | Write getting started guide | Installation and setup | 5.2.1 |
| 5.5.2 | Create module user guides | How to use each module | All modules |
| 5.5.3 | Write import guides | How to import from each source | 2.5 |
| 5.5.4 | Create FAQ documentation | Common questions and answers | All |
| 5.5.5 | Write troubleshooting guide | Common problems and solutions | All |
| 5.5.6 | Create video tutorials | Screen recordings of key features | All |
| 5.5.7 | Write API documentation | For advanced users/developers | 1.4 |
| 5.5.8 | Create privacy documentation | How data is handled | 1.5 |
| 5.5.9 | Write genomics interpretation guide | Understanding genetic results | 3.1 |

---

### 5.6 Testing & Quality Assurance

#### Tasks

| Task ID | Task | Description | Dependencies |
|---------|------|-------------|--------------|
| 5.6.1 | Complete unit test coverage | >80% code coverage | All modules |
| 5.6.2 | Run integration tests | Test module interactions | 5.6.1 |
| 5.6.3 | Perform load testing | Test with large datasets | 5.3.3 |
| 5.6.4 | Conduct user acceptance testing | Real user testing | 5.2.1 |
| 5.6.5 | Test on all platforms | Windows, macOS, Linux | 5.1.4, 5.1.5, 5.1.6 |
| 5.6.6 | Perform accessibility audit | WCAG compliance | All |
| 5.6.7 | Test offline functionality | Verify local-only operation | All |
| 5.6.8 | Create automated regression tests | Prevent regressions | 5.6.1 |

---

### Phase 5 Success Criteria

| Criterion | Verification Method |
|-----------|---------------------|
| Installer works on all platforms | Test on Windows, macOS, Linux |
| Non-technical user can complete setup | User testing with novice users |
| Application launches in <5 seconds | Measure startup time |
| No critical security vulnerabilities | Security audit report |
| Documentation covers all features | Review against feature list |
| 80%+ unit test coverage | Coverage report |
| Application handles 10+ years of data | Load test with sample data |

### Phase 5 Deliverables Checklist

- [ ] Windows installer (.exe)
- [ ] macOS installer (.dmg)
- [ ] Linux packages (AppImage, deb)
- [ ] Auto-update system
- [ ] Installation wizard
- [ ] User onboarding flow
- [ ] Performance optimizations
- [ ] Security audit completed
- [ ] Getting started guide
- [ ] Module user guides
- [ ] FAQ and troubleshooting
- [ ] Video tutorials
- [ ] API documentation
- [ ] Unit test suite (>80% coverage)
- [ ] Integration tests
- [ ] Accessibility compliance

