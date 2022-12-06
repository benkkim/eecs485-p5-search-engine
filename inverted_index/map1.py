#!/usr/bin/env python3
import sys
import csv
import re

csv.field_size_limit(sys.maxsize)
for line in csv.reader(sys.stdin):
    line = [re.sub(r"[^a-zA-Z0-9 ]+", "", word) for word in line]
    doc_id = line[0].strip()
    title_body = line[1] + " " + line[2]
    stopwords = set()
    with open("stopwords.txt", "r") as f:
        for line in f:
            stopwords.add(line.strip())
    title_body = title_body.casefold()
    title_body = title_body.split()
    title_body = [word.strip() for word in title_body if word.strip() not in stopwords]
    title_body = " ".join(title_body)
    sys.stdout.write(f"{doc_id}\t{title_body}\n")
    