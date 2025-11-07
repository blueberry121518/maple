# Maple Backend

This directory contains a layered FastAPI project scaffolded for future development. Each layer isolates concerns such as routing, controllers, services, data access, and configuration.

## Project Structure

```
app/
├── __init__.py            # Exposes the FastAPI `app`
├── main.py                # FastAPI application factory and router wiring
├── api/
│   ├── __init__.py
│   └── router.py          # Aggregates all route controllers
├── controllers/
│   ├── __init__.py
│   ├── agent_controller.py        # WebSocket chat pipeline
│   ├── database_controller.py     # GET /api/fetch/files
│   └── onboarding_controller.py   # GET /api/onboard
├── services/
│   ├── __init__.py
│   ├── agent_gateway.py     # Handles WebSocket event flow
│   ├── database_service.py  # Stub DB access for file listings
│   └── onboarding_service.py
├── crud/
│   ├── __init__.py
│   ├── base_crud.py       # Abstract CRUD helpers
│   └── user_crud.py
├── db/
│   ├── __init__.py
│   ├── base.py            # Declarative base class
│   └── session.py         # SQLAlchemy engine + session factory
├── models/
│   ├── __init__.py
│   └── user_model.py      # SQLAlchemy `User` table
├── schemas/
│   ├── __init__.py
│   ├── agent_schema.py       # WebSocket event contracts
│   └── database_schema.py    # File-tree response models
├── core/
│   ├── __init__.py
│   └── config.py          # Environment-driven settings
└── prompts.py             # Central prompt definitions

.env                       # Environment variables (APP_NAME, DATABASE_URL, DEV_MODE)
requirements.txt           # Python dependencies for the backend
```

## Quickstart

1. Create and activate a virtual environment:
   ```bash
   cd /Users/blueberry/Coding/Projects/maple/backend
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at http://127.0.0.1:8000/ and the interactive docs at http://127.0.0.1:8000/docs.

## Available APIs

- `GET /api/onboard?url=...`
  - Validates the GitHub repository URL and enqueues an asynchronous onboarding job.
  - Responds with `202 Accepted` and an empty body.
- `GET /api/fetch/files?repo_id=...`
  - Returns a placeholder repository snapshot until the real database integration is ready.
- `WS /api/agent/interaction`
  - Establishes a bidirectional WebSocket session with the agent gateway.
  - Accepts `USER_TEXT_MESSAGE` and `TOOL_CALL_SUCCESS` events from the frontend.
  - Emits status, chat, and UI command events back to the client.

## Next Steps

- Replace the stub services with real background workers, database reads, and agent orchestration.
- Implement migrations and persistence for repository metadata and onboarding jobs.
- Harden the WebSocket protocol (authentication, sequencing, persistence).

