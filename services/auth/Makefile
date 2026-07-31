.PHONY: help run test lint format revision migrate downgrade

help:
	@echo "Доступные команды:"
	@echo "  make run                   - Запустить сервис в dev-режиме"
	@echo "  make test                  - Запустить тесты"
	@echo "  make lint                  - Проверить код линтером ruff"
	@echo "  make format                - Отформатировать код с помощью ruff"
	@echo "  make revision msg='...'    - Создать новую миграцию Alembic"
	@echo "  make migrate               - Применить все миграции (upgrade head)"
	@echo "  make downgrade             - Откатить последнюю миграцию (downgrade -1)"

run:
	uv run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

test:
	uv run pytest -v

lint:
	uv run ruff check .

format:
	uv run ruff check . --fix
	uv run ruff format .

revision:
	uv run alembic revision --autogenerate -m "$(msg)"

migrate:
	uv run alembic upgrade head

downgrade:
	uv run alembic downgrade -1
