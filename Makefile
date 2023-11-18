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
docker-build:
	#build container command
	# docker build -t deploy-ml-model .
docker-run:
	#run container command
	# docker run -p 8080:8080 deploy-ml-model
deploy:
	#deploy command
all: install lint test format docker-build docker-run deploy