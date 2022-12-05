#!/usr/bin/env python3
import sys
import itertools
import json
import math

def reduce_one_group(key, group):
    """Reduce one group."""
    file_count = 0
    with open("total_document_count.txt", "r") as file:
        file_count = int(file.readline())
    
    group = list(group)
    for word in group:
        word = word.split()
        if len(word) < 2:
            continue
        tf_k = word[2]
        d_id = float(word[1])
        idf_k = float(math.log10(file_count / len(list(group))))
        w_ik = float(idf_k) * float(tf_k)
        print(f"{key}\t{idf_k} {d_id} {w_ik} {tf_k}")

    

def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()