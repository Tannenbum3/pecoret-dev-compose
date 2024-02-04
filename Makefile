#!/usr/bin/make

include .env

define SERVERS_JSON
{
	"Servers": {
		"1": {
			"Name": "fastapi-alembic",
			"Group": "Servers",
			"Host": "$(DATABASE_HOST)",
			"Port": 5432,
			"MaintenanceDB": "postgres",
			"Username": "$(DATABASE_USER)",
			"SSLMode": "prefer",
			"PassFile": "/tmp/pgpassfile"
		}
	}
}
endef
export SERVERS_JSON

help:
	@echo "make"
	@echo "    install"
	@echo "        Install all packages of poetry project locally. #TODO "
	@echo "    run-dev-build"
	@echo "        Run development docker compose and force build containers."
	@echo "    run-dev"
	@echo "        Run development docker compose."
	@echo "    stop-dev"
	@echo "        Stop development docker compose."
	@echo "    run-prod"
	@echo "        Run production docker compose. #TODO"
	@echo "    stop-prod"
	@echo "        Run production docker compose.#TODO"
	@echo "    init-db"
	@echo "        Init database with sample data."#TODO
	@echo "    add-dev-migration"
	@echo "        Add new database migration using alembic.#TODO"
	@echo "    formatter"
	@echo "        Apply black formatting to code.#TODO"
	@echo "    lint"
	@echo "        Lint code with ruff, and check if black formatter should be applied.#TODO"
	@echo "    lint-watch"
	@echo "        Lint code with ruff in watch mode."
	@echo "    lint-fix"
	@echo "        Lint code with ruff and try to fix."	
	@echo "    run-sonarqube"
	@echo "        Starts Sonarqube container."
	@echo "    run-sonar-scanner"
	@echo "        Starts Sonarqube container."	
	@echo "    stop-sonarqube"
	@echo "        Stops Sonarqube container."

install:
	cd backend/app && poetry install && cd ../..

run-dev-build:
	docker compose -f docker-compose-dev.yml up --build -d

run-dev:
	docker compose -f docker-compose-dev.yml up -d

stop-dev:
	docker compose -f docker-compose-dev.yml down

run-prod:
	docker compose up -d

stop-prod:
	docker compose down

init-db:
	docker compose -f docker-compose-dev.yml exec api_server python manage.py migrate && \
	docker compose -f docker-compose-dev.yml exec api_server createsuperuser --noinput && \
	echo "Initial admin user created and migrated"

add-dev-migration:
	docker compose -f docker-compose-dev.yml exec api_server python manage.py makemigrations && \
	docker compose -f docker-compose-dev.yml exec api_server python manage.py migrate && \
	echo "Migration added and applied."

