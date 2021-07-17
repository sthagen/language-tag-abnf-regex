# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import re

import pytest  # type: ignore

# HACK A DID ACK - todo(sthagen) temporary placement of SUT in below constant
PATTERN = (
    r'^(([A-Za-z]{2,3}(-[A-Za-z]{3}(-[A-Za-z]{3}){0,2})?|[A-Za-z]{4,8})'
    r'(-[A-Za-z]{4})?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*'
    r'(-[A-WY-Za-wy-z0-9](-[A-Za-z0-9]{2,8})+)*(-x(-[A-Za-z0-9]{1,8})+)?|x(-[A-Za-z0-9]{1,8})+|i-default|i-mingo)$')


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
