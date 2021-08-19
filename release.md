# Release Instructions
### Prerequisites:
The release must be done in an environment matching the following criteria:
- GNU `make` is available
- `poetry` is available
- `python` is available, matching the version specified in `pyproject.toml`
- `git` is available

### Doing the release
To do the release from any repo using the common `Makefile` is as simple as running `make release`.

The default behaviour of `make release` will be a dry-run that does not publish any package.

The following environment variables can be set to adjust the behaviour of `make release`:

**NOTE: any changes to the `Makefile` will have to be pushed to `$(BRANCH)` on remote to take effect, even when working locally, as the Makefile clones itself from the remote and switches to that version partway through execution**

|  ENV VARIABLE | USAGE   |
|---|---|
|`RIALTIC_RELEASE_WET_RUN`   | If this is set to `1`, the release will attempt to publish to the configured package repository. The `Makefile` defaults to `https://test.pypi.org/legacy` (the official test repository for PyPI)  |
|`RIALTIC_RELEASE_PYPI` | If this is set to `1` the release will be to the official PyPI repository instead of the test one.  |
| `RIALTIC_PYPI_TOKEN_TEST` | This should contain a valid API token for `test.pypi.org`, used when `${RIALTIC_RELEASE_PYPI} != 1`  |
|  `RIALTIC_PYPI_TOKEN` | This should contain a valid API token for `pypi.org`, used when `${RIALTIC_RELEASE_PYPI} == 1`  |
| `RIALTIC_RELEASE_NONLOCAL` |If this is set to `1`, the makefile will not attempt to use local ssh key for git auth; instead it will expect a token, specified with `RIALTIC_LIBS_PAT`|
|`RIALTIC_LIBS_PAT`| This should be set to a Github Personal Access Token (PAT), that must have read and write access to $(BRANCH) on target repository. It will only be used if `${RIALTIC_RELEASE_NONLOCAL} == 1`|
