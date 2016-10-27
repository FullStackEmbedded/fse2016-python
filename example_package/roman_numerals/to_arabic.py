#!/usr/local/bin/python2.7
# encoding: utf-8

'''Convert Roman numerals to Arabic numerals.'''


from maps import MODERN_NUMBER_MAP
from to_roman import InvalidNumberError


def to_arabic(n):
    """Convert to Arabic numeral."""
    result = 0
    for number, symbol in MODERN_NUMBER_MAP:
        while n.startswith(symbol):
            result += number
            n = n[len(symbol):]
    if n:
        raise InvalidNumberError("Couldn't parse passed symbols.")
    return result
