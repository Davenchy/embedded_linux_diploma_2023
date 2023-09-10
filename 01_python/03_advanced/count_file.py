#!/usr/bin/env python3
"""Counts the number of lines/words in a file."""

import sys
from functools import reduce


def count_file(filename, readlines=True):
    """Counts the number of lines/words in a file.

    Args:
        filename (str): The name of the file.
        readlines (bool): Whether to count lines or words."""

    with open(filename) as f:
        if readlines:
            # count file lines
            return f"{len(f.readlines())} line/s"

        # count words on each file line
        count = reduce(lambda a, b: a + len(b.split()), f.readlines(), 0)
        return f"{count} word/s"


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {} <mode> <filename>'.format(sys.argv[0]))
        print('Modes: lines, words')
        exit(1)

    mode = sys.argv[1]
    filename = sys.argv[2]

    # validate counting mode
    if mode not in {'lines', 'words'}:
        print('Invalid mode: {}'.format(mode), file=sys.stderr)
        exit(1)

    try:
        print(count_file(filename, mode == 'lines'))
    except FileNotFoundError:
        print('File {} not found.'.format(filename), file=sys.stderr)
        exit(1)
    except OSError as err:
        print('Failed to read from file: {}: reason: {}'.format(
            filename, err), file=sys.stderr)
        exit(1)
