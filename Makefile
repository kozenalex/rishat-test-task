MANAGE := poetry run python3 manage.py
.PHONY: shell
shell:
		@$(MANAGE) shell
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
		@$(MANAGE) createsuperuser
.PHONY: test
test:
		@$(MANAGE) test --with-coverage --cover-xml
lint:
		flake8 stripe_buy