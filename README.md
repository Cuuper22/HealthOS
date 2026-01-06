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

