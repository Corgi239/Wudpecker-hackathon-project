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
deploy:
	#deploy command
all: install format lint test deploy