# Update this file from a profile with:
# curl -O https://github.com/open-contracting/standard_profile_template/blob/master/schema/apply-extensions.py

import os
import sys

from ocds_documentation_support import apply_extensions

basedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(basedir, '..', 'docs'))

from conf import profile_identifier, extension_versions  # noqa

apply_extensions(basedir, profile_identifier, extension_versions)
