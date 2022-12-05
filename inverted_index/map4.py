#!/usr/bin/env python3
import sys

for line in sys.stdin:
    text = line.split("\t")
    if len(text) < 2:
        continue
    term = text[0]
    value = text[1].split()
    idf_k = float(value[0])
    d_id = float(value[1])
    w_ik = float(value[2])
    tf_k = float(value[3])
    print(f"{d_id}\t{term} {idf_k} {w_ik} {tf_k}")