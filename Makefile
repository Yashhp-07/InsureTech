.PHONY: dev dev-backend dev-frontend test lint migrate clean

dev:
	@echo "Starting backend..."
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
	@sleep 2
	@echo "Starting frontend..."
	cd frontend && npm run dev

dev-backend:
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

dev-frontend:
	cd frontend && npm run dev

test:
	cd backend && python -m pytest
	cd frontend && npm test

lint:
	cd backend && ruff check . && mypy .
	cd frontend && npx eslint src/

migrate:
	cd backend && alembic upgrade head

clean:
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf frontend/dist/
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
