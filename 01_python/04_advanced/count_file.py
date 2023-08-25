#!/usr/bin/env python3
"""Counts the number of lines/words in a file."""

import sys


def count_file(filename, readlines=True):
    """Counts the number of lines/words in a file.

    Args:
        filename (str): The name of the file.
        readlines (bool): Whether to count lines or words."""

    with open(filename) as f:
        count = 0
        for line in f:
            if readlines:
                count += 1
            else:
                count += len(line.split())
    return count


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {} <mode> <filename>'.format(sys.argv[0]))
        print('Modes: lines, words')
        exit(1)

    mode = sys.argv[1]
    filename = sys.argv[2]
    if mode not in {'lines', 'words'}:
        print('Invalid mode: {}'.format(mode), file=sys.stderr)
        exit(1)

    try:
        print(count_file(filename, mode == 'lines'))
    except FileNotFoundError:
        print('File {} not found.'.format(filename), file=sys.stderr)
        exit(1)
    except Exception:
        print('Failed to read from file: {}'.format(
            sys.exc_info()[0]), file=sys.stderr)
        exit(1)
