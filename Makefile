SHELL := /bin/bash

.PHONY: install
install:
	poetry install


.PHONY: test
test: install
	poetry run pytest tests

.PHONY: build
build: test
	poetry build

.PHONY: clean
clean:
	@rm -r dist