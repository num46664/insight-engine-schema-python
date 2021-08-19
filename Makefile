SHELL := /bin/bash
TEMP_DIR = .tmp
REPO_NAME = 'insight-engine-schema-python'
OUTPUT_DIR = dist
BRANCH = master

ifeq (${RIALTIC_RELEASE_NONLOCAL}, 1)
REMOTE_GIT_URL = "https://${RIALTIC_LIBS_PAT}@github.com/rialtic-community/insight-engine-schema-python.git"
else
REMOTE_GIT_URL = 'git@github.com:rialtic-community/insight-engine-schema-python.git'
endif

ifeq (${RIALTIC_RELEASE_PYPI}, 1)
PUBLISH_CMD = poetry publish
TOKEN = "${RIALTIC_PYPI_TOKEN}"
else
PUBLISH_CMD = poetry publish -r testpypi
TOKEN = "${RIALTIC_PYPI_TOKEN_TEST}"
endif


# <Build>
.PHONY: install
install:
#	install dependencies
	poetry install

.PHONY: test
test: install
#	run tests
	poetry run pytest tests

.PHONY: package
package: install test
#	delete output dir if exists
	@rm -rf $(OUTPUT_DIR)
	poetry build
# </Build>

# <Release>
.PHONY: build-in-place
build-in-place: package
	@echo "-> Build In Place"
	@./check-for-untracked.sh

.PHONY: build-fresh
build-fresh: build-in-place
	@echo "-> Build Fresh"
#	remove temp dir if exists
	rm -rf $(TEMP_DIR)
#	clone repo into temp dir
	git clone $(REMOTE_GIT_URL) $(TEMP_DIR) --branch $(BRANCH)
#	move into temp dir
	$(MAKE) -C $(TEMP_DIR) do-release

.PHONY: release-gatekeep
release-gatekeep: package
	./check-for-untracked.sh

.PHONY: tag
tag: release-gatekeep
	@echo "-> Tag"
	@./tag_and_bump.sh

.PHONY: do-release
do-release: tag
	@echo "-> Do Release"
#	checkout most recent tag
	@git config advice.detachedHead false
	@git checkout $$(git describe --tags `git rev-list --tags --max-count=1`)
	@$(MAKE) -C  .  publish


.PHONY: final-build
final-build: package

.PHONY: publish
publish: final-build
	@poetry config repositories.testpypi https://test.pypi.org/legacy/
	@if [ "${RIALTIC_RELEASE_WET_RUN}" = 1 ]; then \
  		git remote add upstream $(REMOTE_GIT_URL) \
	    && $(PUBLISH_CMD) --username __token__ --password $(TOKEN) \
	    && git checkout $(BRANCH) \
	    && git push upstream $$(git describe --tags `git rev-list --tags --max-count=1`) \
	    && git push upstream $(BRANCH); \
    else \
		$(PUBLISH_CMD) --username __token__ --password $(TOKEN) --dry-run; \
	fi
.PHONY: release
release: build-fresh

# </Release>

.PHONY: clean
clean:
	@rm -r $(OUTPUT_DIR)
	@rm -rf $(TEMP_DIR)
