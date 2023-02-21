MANAGE := poetry run python3 manage.py
.PHONY: shell
shell:
		@$(MANAGE) shell_plus
.PHONY: migrate
migrate:
		@$(MANAGE) makemigrations stripe_buy
		@$(MANAGE) migrate		
.PHONY: install
install:
		@poetry install
.PHONY: run
run:
		@$(MANAGE) runserver
addadmin:
		@$(MANAGE) add_admin
lint:
		flake8 stripe_buy
localstart:
		poetry run gunicorn -b 0.0.0.0:8000 stripe_buy.wsgi
start:
		gunicorn stripe_buy.wsgi
build:
		docker compose build
startdocker:
		docker compose up -d
stopdocker:
		docker compose down