# Issues & Insights Tracker

A minimal full-stack SaaS app to track and manage issues with role-based access, real-time updates, and daily aggregation.

### Video Demo
LINK: https://www.loom.com/share/70f0cf7300904eb8b5836396674c4aed?sid=5dbff3fa-f2a8-42d5-b5be-9ff3a6f50f92

## Features

- User authentication with roles: ADMIN, MAINTAINER, REPORTER
- Role-based permissions:
  - REPORTER: create/view own issues
  - MAINTAINER: triage and update status/tags
  - ADMIN: full CRUD
- Issue workflow: OPEN → TRIAGED → IN_PROGRESS → DONE
- Real-time updates on issue list (SSE)
- Dashboard chart: open issues per severity
- Background job aggregates issue stats every 30 minutes
- Auto-generated API docs at `/api/docs`

## Tech Stack

- **Frontend:** SvelteKit + Tailwind CSS
- **Backend:** FastAPI + SQLAlchemy + Alembic
- **Database:** PostgreSQL
- **Auth:** OAuth2 with JWT
- **Background Jobs:** APScheduler
- **Realtime:** Server-Sent Events (SSE)
- **Containers:** Docker, Docker Compose

## Getting Started

#### Run Backend Locally (Without Docker)

- Set up virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```

- Install dependencies
```
pip install -r backend/requirements.txt
```

- Run FastAPI server
```
PYTHONPATH=backend uvicorn app.main:app --reload
```

### Run Frontend

```
cd frontend
npm install
npm run dev
```

### API Docs
```
Visit: http://localhost:8000/api/docs
```
### Database Migrations
```
cd backend
alembic revision --autogenerate -m "message"
alembic upgrade head
```
### Notes

- Focused only on required features as per assessment.
- Bonus features and deployment are not included.
