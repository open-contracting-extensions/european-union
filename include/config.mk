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
LOCALE_DIR=locale
# Directory in which to build documentation files.
BUILD_DIR=build
# Extra build files or directories.
EXTRA_BUILD_FILES=
# Files that are built and distributed (you may use Bash extended globbing).
DIST_FILES=
# Directory in which to build .pot files.
POT_DIR=$(BUILD_DIR)/locale
# The prefix, if any, to the schema and codelists domains.
DOMAIN_PREFIX=
# Directory containing assets to copy to the build directory (no trailing slash).
ASSETS_DIR=
# The Transifex project name.
TRANSIFEX_PROJECT=

# Compile PO files for codelists and schema to MO files, so that translate_codelists and translate_schema succeed.
.PHONY: compile
compile:
	# pybabel compile --use-fuzzy -d $(LOCALE_DIR) -D schema
	# pybabel compile --use-fuzzy -d $(LOCALE_DIR) -D codelists

# Put local targets below.
