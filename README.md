# Rialtic insight engine schema in Python

This repo contains translation of InsightEngine Request/Response schema to Python.
It uses `fhir.resources` internally (see https://pypi.org/project/fhir.resources/).

One may add this schema as a dependency like this:

```
pip install git+ssh://git@github.com:/rialtic-runtime/insight-engine-schema-python.git@engine-schema#egg=insight-engine-schema-python
```

or add the following line to `requirements.txt`:

```
git+ssh://git@github.com:/rialtic-runtime/insight-engine-schema-python.git@engine-schema#egg=insight-engine-schema-python >= 0.7.0
```
