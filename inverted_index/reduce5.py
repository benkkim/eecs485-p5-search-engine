#!/usr/bin/env python3
import sys
import itertools
import json
import re
import math

def reduce_one_group(key, group):
    """Reduce one group."""
    group = list(group)
    output = {}
    for file in group:
        file = file.strip()
        file = file.split("\t")
        d_id = file[1].strip()
        text = file[2].strip()
        l_o_t = file[2][:file[2].index("]") + 1]
        l_o_t = l_o_t.replace("[", "").replace("]", "").split(",")
        norm = file[2][file[2].index("]") + 2:].strip()
        for text in l_o_t:
            text = text.strip()
            text = text.replace("[", "").replace("]", "").replace("'", "")
            t_k = text.split()[0].strip()
            tf_k = text.split()[1].strip()
            idf_k = text.split()[2].strip()
            if t_k not in output:
                output[t_k] = f"{idf_k} {d_id} {tf_k} {norm}"
            else:
                output[t_k] += f" {d_id} {tf_k} {norm}"
    output = sorted(output.items(), key=lambda x: x[0])
    for term, line in output:
        # remove all the extra spaces, tabs, and newlines
        term = re.sub(r"\s+", " ", term)
        line = re.sub(r"\s+", " ", line)
        sys.stdout.write(f"{term} {line}\n") #{line}\n")

def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()