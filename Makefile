PYTHON = python3
PIP = ${PYTHON} -m pip


.PHONY: default
default: test


.PHONY: test
test:
	${PYTHON} -m unittest discover -s ./tests


.PHONY: install
install:
	${PIP} install . --upgrade
