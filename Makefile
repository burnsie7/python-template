## Makefile

## Update this file with the paths and values for your project

.DEFAULT_GOAL := help

.PHONY: help commit venv-clean venv-init

## Include Makefile configuration file

VIRENV=penv
VIRENV_ACTIVATE=. $(VIRENV)/bin/activate
PYTHON=${VIRENV}/bin/python3

help:
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

venv-init: ## Initialize the python virtual env.
	python3 -m venv ${VIRENV}
	pre-commit install
	${VIRENV_ACTIVATE} && export PYTHONPATH=./src/:$$PYTHONPATH
	${PYTHON} -m pip install -r requirements.txt

clean:  ## Remove all temp content (venv, temp dir..)
	@if [ -d ${VIRENV} ]; then rm -rf $(VIRENV); fi
	@rm -rf ${TEMP_DIR}

app: ## run the application
	${PYTHON} ./src/app/app.py

github-test: ## Testing github script
	${PYTHON} ./src/app/tests/_manual_test_.py

docker-gen-push: ## Regenerating and pushing the docker image upstream
	docker build -t app .
	docker tag app:latest user/app:latest
	docker push user/app:latest