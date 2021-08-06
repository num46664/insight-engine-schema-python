#!/usr/bin/env python

from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="insight_engine_schema-python",
    version="0.8.5",
    author="rialtic-runtime",
    author_email="arseniy.zhizhelev@rialtic.io",
    description="Rialtic Insight Engine Python schema",
    long_description=long_description,
    url="https://github.com/rialtic-runtime/insight-engine-schema-python",
    packages= ['insight_engine_schema'],
    classifiers=[ \
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    requires=[\
        "pytest         (>= 6.2.2)",
        "mypy           (>= 0.800)",
        # "pytest-mypy    (>= 0.8.0)",
        "fhir.resources (== 6.0.0)",
    ]
)
