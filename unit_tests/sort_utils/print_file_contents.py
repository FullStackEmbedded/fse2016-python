#!/bin/env python
# -*- coding: utf-8 -*-

'''
Utilities to print file contents.

All functions have the call signature:
    fun(filename, contents) -> filename, contents, continue

Whereas most functions don't use filename. This is simply a hack to give all
functions a unified API, which would normally be avoided by using storing the
data on an object to avoid having to pass it back and forth without reason.
'''

def print_file(_, contents):
    """Print file contents as stored in the file."""
    print(contents)
    return _, contents, False


def print_upper_case(_, contents):
    """Print file contents in uppercase."""
    print(contents.upper())
    return _, contents, False


def print_lower_case(_, contents):
    """Print file contents in lowercase."""
    print(contents.lower())
    return _, contents, False


def file_backwards(_, contents):
    """Print file contents backwards."""
    print(contents[::-1])
    return _, contents, False


def words_backwards(_, contents):
    """Print file with each word in original order but reversed."""
    split_by_spaces = contents.split(" ")
    # Split chunks that wrap around a line break
    for i, word in enumerate(split_by_spaces):
        if "\n" in word:
            split_by_spaces[i] = word.split("\n")
    i = 0
    while i < len(split_by_spaces):
        if isinstance(split_by_spaces[i], list):
            broken_line = split_by_spaces.pop(i)
            for item in broken_line:
                if not item:
                    item = "\n"
                split_by_spaces.insert(i, item)
                i += 1
        i += 1
    for i, word in enumerate(split_by_spaces):
        split_by_spaces[i] = word[::-1]
    print(" ".join(split_by_spaces))
    return _, contents, False


def choose_file(*args):
    """Choose new file."""
    filename = ""
    while not filename:
        filename = raw_input("What file would you like to process?: ")
        try:
            with open(filename) as my_file:
                contents = my_file.read()
        except IOError:
            print("Invalid file. Please enter a valid filename.")
            filename = ""
    return filename, contents, False


def _exit_program(*args):
    """Exit program."""
    return None, None, True


FUNCTIONS = [print_file,
             print_upper_case,
             print_lower_case,
             file_backwards,
             words_backwards,
             choose_file,
             _exit_program]


def main():
    print(WELCOME_MESSAGE)
    finished, filename, choice = False, False, None
    while not finished:
        if not filename:
            filename, contents, finished = choose_file()
        for i, fun in enumerate(FUNCTIONS):
            print("{}: {}".format(i + 1, fun.__doc__))
        try:
            choice = int(raw_input()) - 1
            if choice < 0 or choice >= len(FUNCTIONS):
                raise ValueError
        except ValueError:
            choice = None
            print("Invalid choice. Please enter a choice from the menu.")
        if choice is not None:
            filename, contents, finished = FUNCTIONS[choice](filename,
                                                             contents)


if __name__ == "__main__":
    main()
