#!/usr/bin/env python3
import sys

for line in sys.stdin:
    text = line.split("\t")
    if len(text) < 2:
        continue
    key = text[0].split()
    t_k = key[1]
    freq = float(text[1])
    d_id = float(key[0])
    print(f"{t_k}\t{d_id} {freq}")