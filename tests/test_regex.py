# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pathlib
import re

import pytest  # type: ignore

ENCODING = 'utf-8'
PATTERN_SOURCE_PATH = pathlib.Path('grammar', 'regular-expression', 'language-tag.regex')
with open(PATTERN_SOURCE_PATH, 'rt', encoding=ENCODING) as pattern_source:
    PATTERN = pattern_source.read()

TAG_SOURCE_ROOT_CENT = pathlib.Path('tests', 'abnfgen', 'language-tag-n-100-s-42')
TAG_SOURCE_ROOT_MILLE = pathlib.Path('tests', 'abnfgen', 'language-tag-n-1000-s-42-skip-1-100')
TAG_SOURCE_NAME_TEMPLATE = 'language-tag-{}.txt'

WELL_KNOWN_TAGS = (
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


def match(pattern: str, text: str):
    """Proxy method to evaluate the pattern match on text."""
    return re.match(pattern, text)


@pytest.mark.parametrize('tag', WELL_KNOWN_TAGS)
def test_ok_match_on_well_known_tags(tag):
    assert match(PATTERN, tag)


def test_nok_do_not_match_empty_tag():
    assert not match(PATTERN, '')


def _process_data(number: tuple[int], dir: pathlib.Path):
    tag_source_path = pathlib.Path(dir, TAG_SOURCE_NAME_TEMPLATE.format(number))
    with open(tag_source_path, 'rt', encoding=ENCODING) as tag_source:
        tag = tag_source.read()
    actual = match(PATTERN, tag)
    if actual is None:
        raise RuntimeError("Failed to match tag (%s) from source (%s)" % (tag, tag_source_path))


@pytest.mark.parametrize('number', tuple(range(1, 101)))
def test_ok_match_on_abnfgen_cases_cent(number):
    _process_data(number, dir=TAG_SOURCE_ROOT_CENT)


@pytest.mark.parametrize('number', tuple(range(101, 1001)))
def test_ok_match_on_abnfgen_cases_mille(number):
    _process_data(number, dir=TAG_SOURCE_ROOT_MILLE)
