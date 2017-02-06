# Makefile for Hugo

HUGOBUILD     = hugo
BUILDDIR      = public
GITHUB_DIR    = ~/project/dormouse.github.io

# User-friendly check for sphinx-build
ifeq ($(shell which $(HUGOBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(HUGOBUILD)' command was not found. Make sure you have Hugo installed.
endif

.PHONY: help clean html git

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  clean      clean the output dir"
	@echo "  html       to make standalone HTML files"

clean:
	rm -rf $(BUILDDIR)/*

html:
	$(HUGOBUILD)
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)."

git:
	@echo
	@echo "Rsync starting..."
	rsync -a $(BUILDDIR)/ ~/project/dormouse.github.io --exclude ".*"
	@echo "Git pull..."
	cd $(GITHUB_DIR) && git pull && git add -A && git commit -m 'update' && git push origin $(GITHUB_PAGES_BRANCH)
	@echo
	@echo "Done."

