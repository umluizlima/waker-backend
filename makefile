.PHONY: environment
environment:
	pyenv install -s 3.10.0
	pyenv uninstall --force wake-up-caller
	pyenv virtualenv 3.10.0 --force wake-up-caller
	pyenv local wake-up-caller
