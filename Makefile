SHELL := /bin/bash
REMOTE_GIT_URL = 'https://github.com/rialtic-community/insight-engine-schema-python.git'
TEMP_DIR = .tmp
REPO_NAME = 'insight-engine-schema-python'
OUTPUT_DIR = dist

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
	@[ -d $(OUTPUT_DIR) ] && rm -r $(OUTPUT_DIR)
	poetry build
# </Build>

# <Release>
.PHONY: build-in-place
build-in-place: package
	@./check-for-untracked.sh && echo 'No untracked files... check!'


.PHONY: dep-check
dep-check: build-in-place
	echo 'SUCESS!!!'

.PHONY: build-fresh
build-fresh: build-in-place
#	remove temp dir if exists
	@rm -rf $(TEMP_DIR)
#	clone repo into temp dir
	git clone $(REMOTE_GIT_URL) $(TEMP_DIR)
	git checkout master
#	move into temp dir
	@$(MAKE) -C $(TEMP_DIR)/$(REPO_NAME) do-release

.PHONY: release-gatekeep
release-gatekeep: package
	./check-for-untracked.sh

.PHONY: tag
tag: release-gatekeep
	./tag_and_bump.sh

.PHONY: do-release
do-release: tag
#	checkout most recent tag
	@git checkout $$(git describe --tags `git rev-list --tags --max-count=1`)
	@$(MAKE) -C  .  finish-release


.PHONY: final-build
final-build: package

.PHONY: finish-release
finish-release: final-build

.PHONY: release
release: build-fresh
	poetry publish --dry-run
# </Release>

.PHONY: clean
clean:
	@rm -r $(OUTPUT_DIR)
