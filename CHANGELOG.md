# Changelog

## [Production-Ready Release] - 2026-02-28

### CRITICAL FIXES

#### Backend

1. **Added CORS Configuration** (Issue #1)
   - Configured CORS middleware to allow frontend (localhost:5173, localhost:3000)
   - Enables credentials, all methods, and all headers

2. **Created .env.example** (Issue #3)
   - Documented all 12+ environment variables
   - Added security warnings for production secrets
   - Included database, JWT, rate limiting, and email configuration

3. **Fixed bcrypt Compatibility** (Issue #4)
   - Pinned bcrypt to version 4.0.1 for Python 3.8+ compatibility
   - Added slowapi and aiosmtplib dependencies

4. **Added Rate Limiting on Auth Endpoints** (Issue #8)
   - Implemented slowapi rate limiting
   - Login/register: 5 requests per minute
   - Password reset request: 3 requests per hour
   - Prevents brute force attacks

5. **Implemented Password Reset** (Issue #9)
   - Added POST /api/auth/password-reset-request endpoint
   - Added POST /api/auth/password-reset endpoint
   - JWT-based reset tokens with 1-hour expiration
   - Email support (logs to console in development)

6. **Added Medication Validation** (Issue #7)
   - Validates dosage for negative values
   - Rejects absurdly high dosages (>100,000)
   - Validates date ranges (end_date must be after start_date)

7. **Added Pagination to List Endpoints** (Issue #14)
   - All list endpoints support skip/limit query parameters
   - Default limit: 100, max: 1000 per request
   - Endpoints: timeline, medications, labs, medical_records

8. **Consistent API Error Format** (Issue #13)
   - Created custom exception handlers
   - All errors return: `{"error": {"code": "...", "message": "...", "status": 422}}`
   - Handles validation errors, HTTP errors, and custom API exceptions

#### Frontend

9. **Wired Frontend Auth to Backend** (Issue #1)
   - Created AuthContext with login/register/logout functions
   - JWT token stored in localStorage
   - Auth state persists across page reloads
   - Automatic token inclusion in all API requests

10. **Connected Login Page** (Issue #1)
    - Form submits to POST /api/auth/login
    - Displays errors from backend
    - Shows loading state during authentication
    - Redirects to dashboard on success

11. **Connected Register Page** (Issue #1)
    - Form submits to POST /api/auth/register
    - Collects first name, last name, email, password
    - Automatically logs in after registration
    - Redirects to dashboard

12. **Fixed Timeline API** (Issue #6)
    - Removed manual user ID input (broken UX)
    - Auto-loads timeline for authenticated user
    - Uses JWT token for authentication
    - Shows loading state while fetching

13. **Updated API Service** (Issue #1)
    - All API calls include Authorization header with JWT
    - Improved error handling with descriptive messages
    - Fixed fetchTimeline to use auth (no manual userId)

14. **Added Loading States** (Issue #11)
    - Login/register buttons show "Signing in..." / "Creating account..."
    - Dashboard and timeline show "Loading..." while fetching
    - Prevents double-submission of forms

15. **Added Error Boundaries** (Issue #12)
    - Catches React render errors gracefully
    - Shows user-friendly error message with reload button
    - Logs errors to console for debugging

16. **Updated Shell Navigation** (Issue #10)
    - Shows user name (or email) when logged in
    - Shows logout button for authenticated users
    - Hides protected routes when not logged in
    - Conditionally renders nav based on auth state

17. **Updated Dashboard** (Issue #10)
    - Displays personalized welcome message with user name
    - Shows quick action links
    - Redirects to login if not authenticated
    - Fetches modules with auth token

18. **Fixed Mobile Responsive** (Issue #17)
    - Added media queries for tablets (768px) and phones (480px)
    - Stacks navigation vertically on mobile
    - Single-column layouts for forms and modules
    - iOS zoom prevention (16px min font size on inputs)

### INFRASTRUCTURE

19. **Created docker-compose.yml** (Issue #15)
    - Single command to start backend + frontend
    - Shared volume for database persistence
    - Environment variable configuration

20. **Added Dockerfiles**
    - Backend: Python 3.12-slim with uvicorn
    - Frontend: Node 20-slim with Vite dev server

21. **Created Database Setup Guide** (Issue #5)
    - DATABASE_SETUP.md with full schema documentation
    - Instructions for SQLite (default) and PostgreSQL
    - Backup/restore procedures
    - Migration guidance with Alembic

22. **Created Seed Data Script** (Issue #16)
    - backend/seed_data.py creates test user + sample data
    - Test account: test@healthos.dev / password123
    - Generates medical records, lab results, medications
    - Creates corresponding timeline events

23. **Updated README.md**
    - Quick start with Docker
    - Manual setup instructions
    - Development workflow
    - Test credentials

### SECURITY

- Rate limiting on authentication endpoints
- CORS protection
- Input validation on all endpoints
- Password hashing with bcrypt
- JWT token expiration
- Consistent error messages (no email enumeration on password reset)

### API CHANGES

**New Endpoints:**
- POST /api/auth/password-reset-request - Request password reset token
- POST /api/auth/password-reset - Reset password with token

**Modified Endpoints:**
- GET /api/timeline/ - Added skip/limit pagination
- GET /api/medications/ - Added skip/limit pagination
- GET /api/labs/ - Added skip/limit pagination
- GET /api/medical-records/ - Added skip/limit pagination

**Breaking Changes:**
- fetchTimeline() no longer accepts userId parameter (uses auth token)

### TESTING

Backend can be tested with:
```bash
cd backend
pip install -r requirements.txt
python seed_data.py  # Create test data
uvicorn app.main:app --reload
```

Frontend can be tested with:
```bash
cd frontend
npm install
npm run dev
```

Full stack with Docker:
```bash
docker-compose up
```

Login at http://localhost:5173/login with:
- Email: test@healthos.dev
- Password: password123
