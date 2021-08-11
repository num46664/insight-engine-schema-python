# TODO: This will not be a dry run in any circumstance...
git tag -m "make auto tag" -a "v$(poetry version -s)" && poetry version patch
# TODO: we need to push this tag, right? Should it be in this script?
# I think it should not, just in the veryu last step (definitely not for dry run)
git push origin --tags

# TODO: Option for doing a dry run: set env var DRYRUN before calling make, like
# prompt> DRYRUN=True make
# Cons: do not now if $(MAKE) -C ... inherits env vars (I would assume so, but needs checking)
if [ "$DRYRUN" != "" ]
then
  # simulate tagging
else
  # do the real tagging
fi

