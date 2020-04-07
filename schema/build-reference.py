import os.path
import re
from glob import glob
from textwrap import dedent


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    content = dedent("""\
    # Codelists

    <!-- Do not edit this file. Instead, edit schema/build-reference.py -->

    For more information on codelists, refer to the [codelists reference](https://standard.open-contracting.org/1.1/en/schema/codelists/) in the OCDS documentation.

    The codelists below are from the OCDS and its extensions, and are provided here for convenience only.

    The CSV codelist files can be downloaded from <https://standard.open-contracting.org/profiles/eu/master/en/_static/patched/codelists/>.

    """)  # noqa: E501

    with open(os.path.join(base_dir, 'docs', 'reference', 'codelists.md'), 'w') as f:
        f.write(content)

        filenames = glob(os.path.join(base_dir, 'schema', 'patched', 'codelists', '*.csv'))
        codelists = [os.path.basename(filename) for filename in filenames]

        for filename in sorted(codelists):
            codelist_name = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', filename.replace('.csv', '')).title()

            f.write('\n## {}\n\n'.format(codelist_name))

            f.write(dedent("""\
            ```eval_rst
               .. csv-table-no-translate::
                  :header-rows: 1
                  :class: codelist-table
                  :file: ../_static/patched/codelists/{}
            ```
            """.format(filename)))


if __name__ == '__main__':
    main()
