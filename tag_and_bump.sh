# only increment minor version number (patch)
git tag -m "make auto tag" -a "v$(poetry version -s)" \
&& poetry version patch \
&& git add pyproject.toml \
&& git commit -m "bump version"
# need to push tag in a later step of the makefile
