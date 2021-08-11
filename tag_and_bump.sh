# TODO: add option for doing a dry run: set env var DRYRUN before calling make, like
# prompt> DRYRUN=True make
# Cons: do not now if $(MAKE) -C ... inherits env vars (I would assume so, but needs checking)
if [ "$DRYRUN" != "" ]
then
  # simulate creating tag here (THIS IS TRICKY)
  # We could do, like, a lightweight tag and remove it in the
  # last step (after poetry publish --dry-run)
  # git tag "v$(poetry version -s)"
  # Later (some other script? makefile?) we can cleanup *all* lightweight tags with
  # git for-each-ref refs/tags/ --format '%(objecttype) %(refname:short)' |
  #    while read ty name; do [ $ty = commit ] && git tag -d $name; done
else
  # TODO: what info put in tag message, I used just a simple msg
  git tag -m "make auto tag" -a "v$(poetry version -s)" && poetry version patch
  # TODO: Do we push it now to git? I would think so...
  git push origin --tags
fi

