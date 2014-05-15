# location of virtualenv to use for installing/developing/testing
ENV = "env"

clean:
	rm -rf *.egg *.egg-info build dist

clean-env: clean
	rm -rf $(ENV)

install: test
	python setup.py install

develop: environment
	. $(ENV)/bin/activate
	python setup.py develop

environment:
	virtualenv $(ENV)

test: environment
	. $(ENV)/bin/activate
	python setup.py test

deploy: test
	python setup.py sdist upload

register:
	python setup.py register
