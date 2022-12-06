#!/usr/bin/env python3
import sys
import itertools
import json
import re
import math

def reduce_one_group(key, group):
    """Reduce one group."""
    group = list(group)
    norm = 0.
    l_o_t = []
    for term in group:
        term = term.strip()
        term = term.split("\t")
        d_id = term[0].strip()
        t_k = term[1].split()[0].strip()
        tf_k = term[1].split()[1].strip()
        idf_k = term[1].split()[2].strip()
        norm += (float(tf_k) * float(idf_k)) ** 2 
        l_o_t.append(f"{t_k} {tf_k} {idf_k}")
    sys.stdout.write(f"{d_id}\t{l_o_t} {norm}\n")


    

def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()