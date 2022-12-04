#!/usr/bin/env python3
import sys
import itertools

def reduce_one_group(key, group):
    """Reduce one group."""
    # intialize inverted index vector
    inverted_index = []
    inverted_index.append(key)

def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()