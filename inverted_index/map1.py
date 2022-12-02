#!/usr/bin/env python3
import sys
import csv
import re

for line in sys.stdin:
    line = line.strip()
    words = line.split(",")
    # take the third column and set it to x
    words = words[2]
    # split the string by space
    words = words.split(" ")
    for word in words:
        # open stopwords.txt
        with open("stopwords.txt") as f:
            stopwords = f.read().splitlines()
            # if the word is a special character, remove it
            if word not in stopwords:
                word = re.sub(r"[^a-zA-Z0-9 ]+", "", word)
                print(word.lower(), 1, sep="\t")