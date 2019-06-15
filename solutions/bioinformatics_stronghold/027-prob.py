"""Solution for Bioinformatics Stronghold Problem ID: PPER

Problem Title: Partial Permutations
Link: http://rosalind.info/problems/pper
"""

import math

input_path = "data/rosalind_prob.txt"
input_file = open(input_path, "r")
seq = input_file.readline().rstrip()
gc_list = input_file.readline().rstrip().split(" ")

n_at = seq.count("A") + seq.count("T")
n_gc = seq.count("C") + seq.count("G")

cmn_logs = []

for gc_content in gc_list:
    gc_prob = float(gc_content) / 2.0
    at_prob = (1.0 - float(gc_content)) / 2.0

    seq_prob = math.pow(gc_prob, n_gc) * math.pow(at_prob, n_at)
    cmn_log = round(math.log(seq_prob, 10), 3)
    cmn_logs.append(str(cmn_log))

print(" ".join(cmn_logs))
