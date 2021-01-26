#!/usr/bin/env python

from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="insight-engine-schema-python",
    version="0.7.0",
    author="rialtic-runtime",
    author_email="arseniy.zhizhelev@adaptive.team",
    description="Rialtic Insight Engine Python schema",
    long_description=long_description,
    url="https://github.com/rialtic-runtime/insight-engine-schema-python",
    packages= ['schema'],
    classifiers=[ \
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    requires=[\
        "pytest         (>= 6.1.2)",
        "mypy           (>= 0.790)",
        # "pytest-mypy    (>= 0.8.0)",
        "fhir.resources (== 5.1.1)", # 6.0.0b11
    ]
)
