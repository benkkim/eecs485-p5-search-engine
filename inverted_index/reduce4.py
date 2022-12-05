#!/usr/bin/env python3
import sys
import itertools
import json
import re
import math

def reduce_one_group(key, group):
    """Reduce one group."""
    group = list(group)
    norm = 0
    term = ""
    idf_k = 0
    tf_k = 0
    lord_please = []
    for val in group:
        val = val.split()
        d_id = val[0]
        term = val[1]
        idf_k = float(val[2])
        w_ik = float(val[3])
        tf_k = float(val[4])
        norm += float(w_ik)**2
        lord_please.append(f"{term} {tf_k} {idf_k}")
    print(f"{d_id}\t{lord_please} {norm}")

    

def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()