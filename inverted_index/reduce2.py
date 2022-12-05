#!/usr/bin/env python3
import sys
import itertools
import json

def reduce_one_group(key, group):
    """Reduce one group."""
    print(key, group)
    for v in group:
        print([json.loads(idx.replace("'", '"')) for idx in v])

def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()