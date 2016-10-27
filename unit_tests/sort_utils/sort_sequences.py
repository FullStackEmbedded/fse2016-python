#!/bin/env python
# -*- coding: utf-8 -*-

'''Sort sequences in different ways.'''


def reverse(l):
    """Reverse the order of elements in a list."""
    new_list = []
    for i in range(1, len(l) + 1):
        new_list.append(l[-i])
    return new_list


def sort(l):
    """Sort the items in a list in ascending order."""
    unsorted = l[:]
    sorted = []
    while unsorted:
        lowest = min(unsorted)
        sorted.append(lowest)
        unsorted.remove(lowest)
    return sorted


def reverse_recursive(l):
    """Reverse the order of elements in a list recursively."""
    if len(l) > 1:
        return [l[-1]] + reverse_recursive(l[:-1])
    return [l[0]]


def sort_recursive(l):
    """Sort the items in a list in ascending order recursively."""
    if len(l):
        lowest = min(l)
        l = l[:]
        l.remove(lowest)
        return [lowest] + sort_recursive(l)
    else:
        return l


if __name__ == "__main__":
    print my_function.__doc__
    my_ints = [1, 2, 3, 4, 5]
    my_strings = ["a", "b", "c", "d"]
    assert [5, 4, 3, 2, 1] == reverse(my_ints) == reverse_recursive(my_ints)
    assert (["d", "c", "b", "a"] == reverse(my_strings) ==
            reverse_recursive(my_strings))
    other_strings = ["d", "a", "l"]
    other_ints = [10, 5, 0]
    assert (["a", "d", "l"] == sort(other_strings) ==
            sort_recursive(other_strings))
    assert [0, 5, 10] == sort(other_ints) == sort_recursive(other_ints)
