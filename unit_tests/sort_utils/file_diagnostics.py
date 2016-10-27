#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Compute metrics on user specified files.'''


def print_file(filename):
    """Print the contents of ``filename`` with trailing whitespace removed."""
    with open(filename) as my_file:
        for line in my_file:
            print(line.rstrip())


def n_chars(filename):
    """Count characters in given file."""
    with open(filename) as my_file:
        contents = my_file.read()
    return len(contents)


def n_letters(filename):
    """Count letters in given file."""
    with open(filename) as my_file:
        return len([char for char in my_file.read() if char.isalpha()])


def n_uppercase(filename):
    """Count uppercase letters in given file."""
    UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ"
    with open(filename) as my_file:
        contents = my_file.read()
    return len([letter for letter in contents if letter in UPPERCASE_LETTERS])


def n_lowercase(filename):
    """Count lowercase letters in given file."""
    return n_letters(filename) - n_uppercase(filename)


def print_summary(filename):
    """Print summary of given file."""
    print("Contents of {}:".format(filename))
    print_file(filename)
    print("{filename} contains {chars} chars, "
          "{alphas} of which are alphanumeric.\n"
          "{lower} are lowercase, {upper} are uppercase"
          ".".format(filename=filename,
                     chars=n_chars(filename),
                     alphas=n_letters(filename),
                     lower=n_lowercase(filename),
                     upper=n_uppercase(filename)))


if __name__ == "__main__":
    finished = False
    while not finished:
        files = []
        print("What file should I print?")
        user_input = True
        while user_input:
            user_input = raw_input("Type a filename or press Enter to quit: ")
            if user_input:
                files.append(user_input)
        for filename in files:
            print_summary(filename)
            raw_input("Press Enter to continue.")
        finished = raw_input("Type anything to quit or "
                             "press Enter to see file contents. ")
    print("That's enough files for today. Bye!")
