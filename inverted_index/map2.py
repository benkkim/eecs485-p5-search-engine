#!/usr/bin/env python3
import sys

for line in sys.stdin:
    text = line.split("\t")
    if len(text) < 2:
        continue
    body = text[1]
    words = body.split()
    for word in words:
        print(f"{text[0]} {word}\t1")