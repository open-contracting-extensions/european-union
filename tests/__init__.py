from collections import OrderedDict

languages = {
    'en': 'English',
}

test_basic_params = OrderedDict([
    ('en', 'OCDS'),
])

test_search_params = [
    ('en', r'found \d+ page\(s\) matching'),
]
