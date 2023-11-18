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
	pylint --disable=C0114,C0115,C0116 *.py &&\
		pylint --disable=C0114,C0115,C0116 **/*.py
test:
	#test command
	python -m pytest -vv --cov=src test/*.py
build:
	#build container command
deploy:
	#deploy command
all: install format lint test build deploy