#!/bin/env python
# -*- coding: utf-8 -*-
'''Test functions from the last exercises.'''


import unittest

from sort_utils import sort_sequences


class KnownResults(unittest.TestCase):

    """Check that results match what we expect."""

    ints = [62, 87, 87, 10, 83, 54, 2, 1, 87, 50]
    sorted_ints = [1, 2, 10, 50, 54, 62, 83, 87, 87, 87]
    reversed_ints = [50, 87, 1, 2, 54, 83, 10, 87, 87, 62]
    strs = ["That's", "no", "moon.", "It's", "a", "space", "station."]
    sorted_strs = ["It's", "That's", 'a', 'moon.', 'no', 'space', 'station.']
    reversed_strs = ['station.', 'space', 'a', "It's", 'moon.', 'no', "That's"]

    def test_sorting(self):
        """Known sorting results."""
        self.assertEqual(self.sorted_ints, sort_sequences.sort(self.ints))
        self.assertEqual(self.sorted_ints,
                         sort_sequences.sort_recursive(self.ints))
        self.assertEqual(self.sorted_strs, sort_sequences.sort(self.strs))
        self.assertEqual(self.sorted_strs,
                         sort_sequences.sort_recursive(self.strs))

    def test_reversing(self):
        """Known reversed lists."""
        self.assertEqual(self.reversed_ints, sort_sequences.reverse(self.ints))
        self.assertEqual(self.reversed_ints,
                         sort_sequences.reverse_recursive(self.ints))
        self.assertEqual(self.reversed_strs, sort_sequences.reverse(self.strs))
        self.assertEqual(self.reversed_strs,
                         sort_sequences.reverse_recursive(self.strs))

if __name__ == "__main__":
    unittest.main()
