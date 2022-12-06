#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    line = line.strip()
    text = line.split("\t")
    d_id = text[0].strip()
    idx = int(float(d_id)) % 3
    sys.stdout.write(f"{idx}\t{line}\n")