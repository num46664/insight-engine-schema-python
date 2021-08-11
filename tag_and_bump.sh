VERSION=$(poetry version -s)
git tag "$VERSION"
poetry version patch

