"""Solution for Bioinformatics Stronghold Problem ID: KMP

Problem Title: Speeding Up Motif Finding
Link: http://rosalind.info/problems/kmp
"""

import itertools
from rosalindutils.fasta_parser import FastaParser

input_path = "data/rosalind_kmp.txt"
output_path = "output/rosalind_kmp.output.txt"
seq_objs = FastaParser(input_path).parse_fasta()
seq = seq_objs[0]["sequence"]

prefix_idx = 0
failure_array = ["0"]
failure_num = 0

for i in range(1, len(seq)):

    if seq[i] == seq[prefix_idx]:
        failure_num = prefix_idx + 1
        prefix_idx += 1
    else:
        # no match, how far back in the prefix must we go to get the largest
        # match?
        jumpback_not_reached = True

        while prefix_idx > 0 and jumpback_not_reached:
            # iterate back through the prefix and subseq to find the largest
            # possible match at the current site
            failure_num -= 1
            prefix_idx -= 1

            jumpback_seq = seq[i - failure_num: i + 1]
            jumpback_prefix_seq = seq[0: prefix_idx + 1]

            if jumpback_seq == jumpback_prefix_seq:
                jumpback_not_reached = False
                failure_num = prefix_idx + 1
                prefix_idx += 1

    failure_array.append(str(failure_num))

open(output_path, "w").write(" ".join(failure_array) + "\n")
