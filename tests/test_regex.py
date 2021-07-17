# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pathlib
import re

import pytest  # type: ignore

ENCODING = 'utf-8'
PATTERN_SOURCE_PATH = pathlib.Path('grammar', 'regular-expression', 'language-type.regex')
with open(PATTERN_SOURCE_PATH, 'rt', encoding=ENCODING) as pattern_source:
    PATTERN = pattern_source.read()


def match(pattern: str, text: str):
    """Proxy method to evaluate the pattern match on text."""
    return re.match(pattern, text)


def test_ok_match_on_well_known_tags():
    well_known_tags = (
        'de',
        'de-CH',
        'de-DE-1901',
        'es-419',
        'sl-IT-nedis',
        'en-US-boont',
        'mn-Cyrl-MN',
        'x-fr-CH',
        'en-GB-boont-r-extended-sequence-x-private',
        'sr-Cyrl',
        'sr-Latn',
        'hy-Latn-IT-arevela',
        'zh-TW',
    )
    for tag in well_known_tags:
        assert match(PATTERN, tag)


def test_nok_do_not_match_empty_tag():
    assert not match(PATTERN, '')
