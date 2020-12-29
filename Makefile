POETRY ?= $(HOME)/.poetry/bin/poetry

.PHONY: install-poetry
install-poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

.PHONY: install-packages
install-packages:
	$(POETRY) install -vv

.PHONY: install
install: install-poetry install-packages

.PHONY: run-local
run-local:
	env $$(cat .env-local | xargs) poetry run python gallery/manage.py runserver 0.0.0.0:8010

.PHONY: run-prod
run-prod:
	poetry run python gallery/manage.py runserver 0.0.0.0:8010