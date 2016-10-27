#!/bin/env python
# -*- coding: utf-8 -*-

"""Tests for roman_numerals."""

import unittest

from roman_numerals import to_roman, to_arabic
from roman_numerals.to_roman import InvalidNumberError, ANCIENT_NUMBER_MAP

class ExpectedErrors(unittest.TestCase):

    """Check that illegal conversions are blocked."""

    def test_invalid_roman_conversion(self):
        """
        Both simple and complex Roman numeral functions fail on non-integers.
        """
        self.assertRaises(InvalidNumberError, to_roman, 0)
        self.assertRaises(InvalidNumberError, to_roman, -5)
        self.assertRaises(InvalidNumberError, to_roman, 5.3)

    def test_invalid_arabic_conversion(self):
        """Only known symbols can be parsed."""
        self.assertRaises(InvalidNumberError, to_arabic, "invalid")


class ExpectedResults(unittest.TestCase):

    """Check that correct results are returned."""

    def test_arabic_conversion(self):
        """Known values are converted correctly to Arabicnumerals."""
        self.assertEqual(1984, to_arabic("MDCCCCLXXXIIII"))
        self.assertEqual(1984, to_arabic("MCMLXXXIV"))

    def test_roman_conversion(self):
        """Known values are converted correctly to Roman numerals."""
        self.assertEqual("MDCCCCLXXXIIII", to_roman(1984, ANCIENT_NUMBER_MAP))
        self.assertEqual("MCMLXXXIV", to_roman(1984))


if __name__ == "__main__":
    unittest.main()
