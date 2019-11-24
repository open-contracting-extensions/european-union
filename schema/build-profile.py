import os
import sys

from ocdsextensionregistry import build_profile

basedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(basedir, '..', 'docs'))

from conf import standard_tag, standard_version, extension_versions, schema_base_url  # noqa

build_profile(basedir, standard_tag, extension_versions, schema_base_url=schema_base_url)
