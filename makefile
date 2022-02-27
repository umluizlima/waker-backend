.PHONY: environment
environment:
	pyenv install -s 3.10.0
	pyenv uninstall --force waker
	pyenv virtualenv 3.10.0 --force waker
	pyenv local waker

.PHONY: install
install:
	pip freeze | xargs -r pip uninstall -y
	python -m pip install --upgrade pip
	pip install -r requirements-dev.txt
	pre-commit install

.PHONY: lint
lint:
	isort --check .
	black --check .
	flake8 .

.PHONY: db_init
db_init:
	docker-compose up -d database

.PHONY: db_run_migrations
db_run_migrations: db_init
	PYTHONPATH=. \
	alembic upgrade head

.PHONY: db_generate_migration
db_generate_migration: db_run_migrations
	PYTHONPATH=. \
	alembic revision --autogenerate -m "$(description)"

.PHONY: db_setup_worker
db_setup_worker: db_init
	PYTHONPATH=. procrastinate --app=app.worker.run.worker schema --apply || true

.PHONY: test
test:
	docker-compose down && \
	PYTHONPATH=. ENV=test \
	python -m pytest

.PHONY: run_api
run_api: db_run_migrations
	uvicorn --reload --port=8001 app.api.run:api

.PHONY: run_worker
run_worker: db_setup_worker
	PYTHONPATH=. procrastinate --verbose --app=app.worker.run.worker worker

.PHONY: run
run:
	make -j run_api run_worker
