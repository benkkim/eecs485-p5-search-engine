#!/usr/bin/env python3
import sys
import csv
import re

for line in sys.stdin:
    line = line.strip()
    words = line.split(",")

    # take the third column and set it to x
    doc_id = words[0]
    doc_id = re.sub(r"[^a-zA-Z0-9 ]+", "", doc_id)

    # combine the second and third column and set it to y
    text = words[1] + " " + words[2]

    # text = text.replace('"', '')
    text = re.sub(r"[^a-zA-Z0-9 ]+", "", text)
    text = text.lower()

    #remove stopwords
    text = text.split()
    with open("stopwords.txt", "r") as f:
        stopwords = f.read().splitlines()
        stopwords = set(stopwords)
        text = [word for word in text if word not in stopwords]
    
    
    text = " ".join(text)

    # print a key value pair of doc_id and text
    print(f"{doc_id}\t{text}")