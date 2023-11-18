.PHONY: test

install:
	#install command
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format command
	black *.py &&\
		black **/*.py
lint:
	#lint command
	pylint *.py &&\
		pylint **/*.py
test:
	#test command
	python -m pytest -vv --cov=src test/*.py
deploy:
	#deploy command
all: install format lint test deploy