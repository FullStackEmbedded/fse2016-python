#!/bin/env python
# -*- coding: utf-8 -*-

'''Use all utilities in the other modules in this package.'''

import file_diagnostics as diagnostics
import sort_sequences
from print_file_contents import (choose_file, print_file, print_upper_case,
                                 file_backwards)


def print_file_diagnostics(filename):
    """Print some diagnostics on a given file."""
    summary_template = """
Filename:  {filename}
Chars:     {nchars}
Letters:   {nletters}
Uppercase: {upper}
Lowercase: {lower}
"""[1:-1]
    print(summary_template.format(filename=filename, 
                                  nchars=diagnostics.n_chars(filename),
                                  nletters=diagnostics.n_letters(filename),
                                  upper=diagnostics.n_uppercase(filename),
                                  lower=diagnostics.n_lowercase(filename)))

def main():
    print("Give me 3 files to process.")
    file_list = []
    for i in range(3):
        file_list.append(choose_file())
    filenames = [item[0] for item in file_list]
    file_contents = [item[1] for item in file_list]
    print("You asked me to work on these files:")
    for filename in filenames:
        print(filename)
    print("In alphabetical order, that's:")
    for filename in sort_sequences.sort(filenames):
        print(filename)
    print("Backwards, that's:")
    for filename in sort_sequences.reverse(filenames):
        print(filename)
    print("Let's summarize each file.")
    for filename in filenames:
        print_file_diagnostics(filename)
    print("Last file in original, upper case and backwards:")
    contents = file_contents[-1]
    print_file(None, contents)
    print_upper_case(None, contents)
    file_backwards(None, contents)
    print("That's it! I used all the modules.")

if __name__ == "__main__":
    main()
