#!/usr/bin/env python3
import sys
import csv
import re

for line in sys.stdin:
    line = line.strip()
    words = line.split(",")
    # take the third column and set it to x
    doc_id = words[0]
    # combine the second and third column and set it to y
    text = words[1] + " " + words[2]
    text = text.replace('"', '')
    text = re.sub(r"[^a-zA-Z0-9 ]+", "", text)
    doc_id = doc_id.replace('"', '')
    # print(text)
    # print(doc_id)
    # # split the string by space
    # words = words.split(" ")
    # for word in text:
    #     # make all words lowercase
    #     word = word.lower()
    #     # open stopwords.txt
    #     with open("stopwords.txt") as f:
    #         stopwords = f.read().splitlines()
    #         # if the word is in stopwords.txt, remove it
    #         if word in stopwords:
    #             text = text.replace(word, "")
    
    # print a key value pair of doc_id and text
    print(f"{doc_id}\t{text}")