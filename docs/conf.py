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
import os
from glob import glob
from pathlib import Path

import standard_theme
from ocds_babel.translate import translate
from recommonmark.transform import AutoStructify


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
    'recommonmark',
    'sphinxcontrib.jsonschema',
    'sphinxcontrib.opendataservices',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'standard_theme'
html_theme_path = [standard_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Local configuration -----------------------------------------------------

profile_identifier = 'eu'
repository_url = 'https://github.com/open-contracting-extensions/european-union'

html_theme_options = {
    'display_version': False,
    'root_url': '/profiles/{}'.format(profile_identifier),
    'short_project': project.replace('Open Contracting Data Standard', 'OCDS'),
    'copyright': copyright,
    'license_name': 'Apache License 2.0',
    'license_url': '{}/blob/HEAD/LICENSE'.format(repository_url),
    'repository_url': repository_url,
}

# The version of OCDS to patch.
standard_tag = '1__1__4'
standard_version = '1.1'

# Where the patched schemas will be deployed.
schema_base_url = 'https://standard.open-contracting.org{}/schema/{}/'.format(
    html_theme_options['root_url'], release.replace('-', '__').replace('.', '__'))

# The `LOCALE_DIR` from `config.mk`, plus the theme's locale.
locale_dirs = ['locale/', os.path.join(standard_theme.get_html_theme_path(), 'locale')]

gettext_compact = False

# The `DOMAIN_PREFIX` from `config.mk`.
gettext_domain_prefix = '{}-'.format(profile_identifier)

# List the extension identifiers and versions that should be part of this profile. The extensions must be available in
# the extension registry: https://github.com/open-contracting/extension_registry/blob/master/extension_versions.csv
extension_versions = {
    'additionalContactPoint': 'master',
    'bids': 'v1.1.4',
    'charges': 'master',
    'finance': 'master',
    'location': 'v1.1.4',
    'lots': 'v1.1.4',
    'metrics': 'master',
    'participation_fee': 'v1.1.4',
    'partyScale': 'master',
    'process_title': 'v1.1.4',
    'shareholders': 'master',
    # EU
    'awardCriteria': 'master',
    'bidOpening': 'master',
    'communication': 'master',
    'contractTerms': 'master',
    'coveredBy': 'master',
    'designContest': 'master',
    'eu': 'master',
    'options': 'master',
    'organizationClassification': 'master',
    'otherRequirements': 'master',
    'procedure': 'master',
    'procurementMethodRationaleClassifications': 'master',
    'secondStageDescription': 'master',
    'selectionCriteria': 'master',
    'subcontracting': 'master',
    'submissionTerms': 'master',
    'techniques': 'master',
    'unstructuredChanges': 'master',
}


def setup(app):
    app.add_config_value('extension_versions', extension_versions, True)
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
        'enable_eval_rst': True
    }, True)

    app.add_transform(AutoStructify)

    # The root of the repository.
    basedir = Path(os.path.realpath(__file__)).parents[1]
    # The `LOCALE_DIR` from `config.mk`.
    localedir = basedir / 'docs' / 'locale'

    language = app.config.overrides.get('language', 'en')

    headers = ['Title', 'Description', 'Extension']
    # The gettext domain for schema translations. Should match the domain in the `pybabel compile` command.
    schema_domain = '{}schema'.format(gettext_domain_prefix)
    # The gettext domain for codelist translations. Should match the domain in the `pybabel compile` command.
    codelists_domain = '{}codelists'.format(gettext_domain_prefix)

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
