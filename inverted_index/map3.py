#!/usr/bin/env python3
"""maps term to docid and freq."""
import sys

for line in sys.stdin:
    line = line.strip()
    text = line.split("\t")
    key = text[0].split()
    t_k = key[1].strip()
    freq = text[1].strip()
    d_id = key[0].strip()
    sys.stdout.write(f"{t_k}\t{d_id} {freq}\n")
