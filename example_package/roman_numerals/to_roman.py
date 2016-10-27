#!/usr/local/bin/python2.7
# encoding: utf-8

'''Convert Arabic numerals to Roman numerals.'''


from maps import ANCIENT_NUMBER_MAP, MODERN_NUMBER_MAP


class InvalidNumberError(Exception):
    """Invalid conversion to a Roman numeral."""


def validate_numeral(n):
    """Only allow positive integers."""
    if n <= 0:
        raise InvalidNumberError("Roman numerals must be > 0.")
    if not float(n).is_integer():
        raise InvalidNumberError("Roman numerals must be integers.")


def to_roman(n, number_map=MODERN_NUMBER_MAP):
    """
    Convert to modern Roman numeral.

    The user can choose a number-to-letter map. By default, the modern
    letters are used for conversion, but the user can specify their own map
    in the form of a tuple of two-tuples consisting of numbers and their
    corresponding symbols. 1 such extra map is provided in this module that
    makes it possible to compute Roman numerals using the ancient method.
    """
    validate_numeral(n)
    result = ""
    for number, symbol in number_map:
        while n >= number:
            result += symbol
            n -= number
    return result
