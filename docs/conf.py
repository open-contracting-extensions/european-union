# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import json
import os
from glob import glob
from pathlib import Path

import standard_theme
from docutils.nodes import make_id
from ocds_babel.translate import translate
from sphinx.locale import get_translation

# -- Project information -----------------------------------------------------

project = 'Open Contracting Data Standard for European Union'
copyright = 'Open Contracting Partnership'
author = 'Open Contracting Partnership'

version = '1.0'
release = '1.0.0-rc.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinxcontrib.jsonschema',
    'sphinxcontrib.opendataservices',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**/docson/[!p]**', '**/docson/package*.json']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'standard_theme'  # 'pydata_sphinx_theme'
html_theme_path = [standard_theme.get_html_theme_path()]
html_favicon = '_static/favicon-16x16.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Local configuration -----------------------------------------------------

_ = get_translation('theme')

profile_identifier = 'eu'
repository_url = 'https://github.com/open-contracting-extensions/european-union'

# Internationalization.
gettext_compact = False
# `DOMAIN_PREFIX` from `config.mk`.
gettext_domain_prefix = f'{profile_identifier}-' if profile_identifier else ''
locale_dirs = ['locale/', os.path.join(standard_theme.get_html_theme_path(), 'locale')]
# We use single quotes for codes, which docutils will change to double quotes.
# https://sourceforge.net/p/docutils/code/HEAD/tree/trunk/docutils/docutils/utils/smartquotes.py
smartquotes = False

# MyST configuration.
myst_enable_extensions = ['linkify']
myst_heading_anchors = 6
myst_heading_slug_func = make_id

# Theme customization.
navigation_with_keys = False  # restore the Sphinx default
html_context = {
    'analytics_id': 'HTWZHRIZ',
}
html_theme_options = {
    'analytics_id': 'HTWZHRIZ',
    'display_version': False,
    'root_url': f'/profiles/{profile_identifier}' if profile_identifier else '',
    'short_project': project.replace('Open Contracting Data Standard', 'OCDS'),
    'copyright': copyright,
    'license_name': 'Apache License 2.0',
    'license_url': f'{repository_url}/blob/HEAD/LICENSE',
    'repository_url': repository_url,
}
html_short_title = f'{html_theme_options["short_project"]} v{release}'

# Imported by manage.py.
standard_tag = '1__1__5'  # the version of OCDS to patch
standard_version = '1.1'
managed_codelist = True
# List the extension identifiers and versions that should be part of this specification. The extensions must be in
# the extension registry: https://github.com/open-contracting/extension_registry/blob/main/extension_versions.csv
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'extension_versions.json')) as f:
    extension_versions = json.load(f)


def setup(app):
    # The root of the repository.
    basedir = Path(__file__).resolve().parents[1]
    # `LOCALE_DIR` from `config.mk`.
    localedir = basedir / 'docs' / 'locale'

    language = app.config.overrides.get('language', 'en')

    headers = ['Title', 'Description', 'Extension']
    # The gettext domain for schema translations. Should match the domain in the `pybabel compile` command.
    schema_domain = f'{gettext_domain_prefix}schema'
    # The gettext domain for codelist translations. Should match the domain in the `pybabel compile` command.
    codelists_domain = f'{gettext_domain_prefix}codelists'

    patched_dir = basedir / 'schema' / 'patched'
    profile_dir = basedir / 'schema' / 'profile'
    patched_build_dir = basedir / 'docs' / '_static' / 'patched'
    profile_build_dir = basedir / 'build' / language

    translate([
        # The glob patterns in `babel_ocds_schema.cfg` should match these filenames.
        (glob(str(patched_dir / '*-schema.json')), patched_build_dir, schema_domain),
        (glob(str(profile_dir / '*-schema.json')), profile_build_dir, schema_domain),
        # The glob patterns in `babel_ocds_codelist.cfg` should match these.
        (glob(str(patched_dir / 'codelists' / '*.csv')), patched_build_dir / 'codelists', codelists_domain),
        (glob(str(profile_dir / 'codelists' / '*.csv')), profile_build_dir / 'codelists', codelists_domain),
    ], localedir, language, headers, version=standard_version)

    # Copy the untranslated extension.json file.
    with (profile_dir / 'extension.json').open() as f:
        extension_json = f.read()
    with (profile_build_dir / 'extension.json').open('w') as f:
        f.write(extension_json)
