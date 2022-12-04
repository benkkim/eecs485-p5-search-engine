#!/usr/bin/env python3
import sys

# make a dictionary where the key is the word and the value is a tuple of the doc_id and the count
word_dict = {}

# for each line in the input
for line in sys.stdin:
    doc_id = line[0]
    # remove everything before the tab
    line = line[1:]
    for word in line:
        # if the word is not in the dictionary, add it and set the value to 1
        if word not in word_dict:
            word_dict[word] = (doc_id, 1)
        # if the word is in the dictionary, add 1 to the count
        else:
            word_dict[word] = (doc_id, word_dict[word][1] + 1)
        # print the key value pair
        print(f"{word}\t{doc_id} {word_dict[word][1]}")