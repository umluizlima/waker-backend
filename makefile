.PHONY: environment
environment:
	pyenv install -s 3.10.0
	pyenv uninstall --force wake-up-caller
	pyenv virtualenv 3.10.0 --force wake-up-caller
	pyenv local wake-up-caller

.PHONY: install
install:
	pip freeze | xargs -r pip uninstall -y
	python -m pip install --upgrade pip
	pip install -r requirements-dev.txt
	pre-commit install

.PHONY: run
run:
	PYTHONPATH=. python app
