import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="insight-engine-schema-python",
    version="0.6.1",
    author="rialtic-runtime",
    author_email="arseniy.zhizhelev@adaptive.team",
    description="Rialtic Insight Engine Python schema",
    long_description=long_description,
    url="https://github.com/rialtic-runtime/insight-engine-schema-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
