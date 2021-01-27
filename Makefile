SHELL := /bin/bash

CURDIR = $(shell pwd)

VENV = $(CURDIR)/.venv

json-schema-to-class-bin = $(VENV)/bin/json-schema-to-class
pytest-bin = $(VENV)/bin/pytest

.DEFAULT_GOAL := all

.ONESHELL:

.PHONY: clean python-requirements update-schema-pythonBeans

clean:
	@rm -Rf output

$(VENV):
	python3 -m venv $(VENV)

$(json-schema-to-class-bin): $(VENV)
	source $(VENV)/bin/activate
	pip install json-schema-to-class

$(pytest-bin): $(VENV)
	source $(VENV)/bin/activate
	pip install pytest

python-requirements: $(VENV)
	source $(VENV)/bin/activate
	pip install -r requirements.txt

# json-schema-to-class works. It produces a slightly different schema
# It also requires some minor changes to the schema itself.
# Currently yacg is being used, because it works without schema modification.
update-schema-using-json-schema-to-class: $(json-schema-to-class-bin)
	source $(VENV)/bin/activate
	json-schema-to-class ../insight-engine-schema-python/request.json --indent 2 -o request.py
	json-schema-to-class ../insight-engine-schema-python/response.json --indent 2 -o response.py

update-schema-old:
	@docker pull okieoth/yacg:0.2.1
	@mkdir resources
	@cp ../insight-engine-schema-python/request.json resources/request.json
	@cp ../insight-engine-schema-python/response.json resources/response.json
	@docker run -v `pwd`/resources:/resources --rm -t okieoth/yacg:0.2.1 \
	    --models /resources/request.json  \
                     /resources/response.json \
	    --singleFileTemplates plantUml=stdout


update-schema-pythonBeans: ../insight-engine-schema-python
	@docker pull okieoth/yacg:0.2.1
	@mkdir -p schema
	@cp ../insight-engine-schema-python/request.json schema/request.json
	@cp ../insight-engine-schema-python/response.json schema/response.json
	@docker run -v `pwd`:/workspace --rm -t okieoth/yacg:0.2.1 \
	    --models /workspace/schema/request.json  \
	             /workspace/schema/response.json \
	    --singleFileTemplates pythonBeans=/workspace/schema/insight_engine_schema.py
	@rm schema/request.json
	@rm schema/response.json

update-schema: update-schema-pythonBeans

schema/insight_engine_schema.py: 
	$(MAKE) update-schema-pythonBeans

test:
	source $(VENV)/bin/activate
	pytest schema/test_schema.py

install-requirements:
	source $(VENV)/bin/activate
	pip install -r requirements.txt

all: test
