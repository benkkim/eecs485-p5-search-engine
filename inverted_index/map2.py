#!/usr/bin/env python3
import sys

"""
{
    t_k: [{
            doc_id: doc_id,
            tf: tf
        }]
}
"""

word_dict = {}
for line in sys.stdin:
    line = line.strip()
    words = line.split("\t")
    doc_id = words[0]
    text = words[1]
    text = text.split(" ")
    # print(text)
    for t_k in text:
        if t_k not in word_dict:
            int_dict = {}
            int_dict["d_id"] = doc_id
            int_dict["tf"] = 1
            word_dict[t_k] = [int_dict]
        else:
            for d_id_dict in word_dict[t_k]:
                if d_id_dict["d_id"] == doc_id:
                    d_id_dict["tf"] += 1
                    break
            else:
                int_dict = {}
                int_dict["d_id"] = doc_id
                int_dict["tf"] = 1
                word_dict[t_k].append(int_dict)
for k, v in word_dict.items():
    print(f"{k}\t{v}")

            