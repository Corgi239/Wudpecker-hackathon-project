install:
	#install command
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format command
lint:
	#lint command
test:
	#test command
deploy:
	#deploy command
all: install format lint test deploy