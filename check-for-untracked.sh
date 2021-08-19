if [ -z "$(git status --porcelain)" ]; then
  # Working directory clean
  exit 0
else
  # Uncommitted changes
  echo "!!!"
  echo "ERROR: Uncommitted changes in repo; aborting release"
  echo "!!!"
  git status
  exit 1
fi
