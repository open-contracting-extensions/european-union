# Compare this file to:
# https://github.com/open-contracting/standard_profile_template/blob/master/include/config.mk

# Edit these variables as appropriate.

# The space-separated, period-prefixed translations to build (for easier substitutions).
TRANSLATIONS=
# The source language and translations to build.
LANGUAGES=.en $(TRANSLATIONS)

# Directory of documentation files to build with Sphinx.
DOCS_DIR=docs
# Directory of catalog files.
LOCALE_DIR=docs/locale
# Directory in which to build documentation files.
BUILD_DIR=build
# Extra build files or directories. (These should match paths in .gitignore.)
EXTRA_BUILD_FILES=chromedriver* docs/_static/patched
# Files that are built and distributed (you may use Bash extended globbing).
DIST_FILES=schema/profile/release-schema.json schema/profile/codelists schema/patched
# Directory in which to build .pot files.
POT_DIR=$(BUILD_DIR)/locale
# The prefix, if any, to the schema and codelists domains.
DOMAIN_PREFIX=
# The Transifex project name.
TRANSIFEX_PROJECT=
# Any additional extract targets.
EXTRACT_TARGETS=

# The path to the branch of the documentation to print to PDF.
PDF_ROOT=/profiles/eu/master
# The pattern of pages to print to PDF. Update if the documentation adds, removes or renames pages.
PDF_PAGES={,F01/,F02/,F03/,F04/,F05/,F06/,F07/,F08/,F12/,F13/,F14/,F15/,F20/,F21/,F22/,F23/,F24/,F25/,T01/,T02/,common/,operations/,changelog/}
# 15000 may warn: "Warning: Received createRequest signal on a disposed ResourceObject's NetworkAccessManager. This might
# be an indication of an iframe taking too long to load."
PDF_DELAY=20000

# Compile PO files for codelists and schema to MO files, so that `translate` succeeds.
.PHONY: compile
compile:
	# pybabel compile --use-fuzzy -d $(LOCALE_DIR) -D $(DOMAIN_PREFIX)schema
	# pybabel compile --use-fuzzy -d $(LOCALE_DIR) -D $(DOMAIN_PREFIX)codelists

# Put local targets below.
