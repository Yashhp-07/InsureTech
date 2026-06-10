# InsureTech

Insurance technology platform.

## Tech Stack

- **Backend**: FastAPI, SQLAlchemy 2.0, asyncpg, Alembic
- **Frontend**: React, TypeScript, Vite
- **Database**: PostgreSQL
- **CI/CD**: GitHub Actions

## Prerequisites

- Python 3.12+
- Node.js 20+
- PostgreSQL 16+

## Setup

```bash
git clone https://github.com/<org>/InsureTech.git
cd InsureTech

# Backend
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
# Edit .env with your PostgreSQL credentials

# Frontend
cd ../frontend
npm install

# Database
createdb insuretech
cd ../backend && alembic upgrade head
```

## Development

```bash
make dev          # Start both backend and frontend
make dev-backend  # Start backend only (localhost:8000)
make dev-frontend # Start frontend only (localhost:5173)
make test         # Run all tests
make lint         # Lint and type-check
make migrate      # Run database migrations
```

## Branch Strategy

- `main` – production
- `staging` – pre-release testing
- `develop` – integration
- `feature/*` – feature work (branch from develop)

## Architecture

```
backend/            FastAPI modular monolith
  app/core/         Shared infrastructure (config, db, auth)
  app/modules/      Domain modules (users, policies, claims)
frontend/           React SPA
  src/api/          API client
  src/components/   Reusable UI components
  src/pages/        Page components
```
