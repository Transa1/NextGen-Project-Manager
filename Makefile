.PHONY: up down build logs migrate revision shell

up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

logs:
	docker-compose logs -f api

migrate:
	docker-compose exec api alembic upgrade head

revision:
	docker-compose exec api alembic revision --autogenerate -m "$(m)"

shell:
	docker-compose exec api bash