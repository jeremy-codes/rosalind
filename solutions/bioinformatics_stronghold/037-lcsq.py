"""Solution for Bioinformatics Stronghold Problem ID: LCSQ

Problem Title: Finding a Shared Spliced Motif
Link: http://rosalind.info/problems/lcsq
"""

import sys
import itertools
from rosalindutils.fasta_parser import FastaParser

sys.setrecursionlimit(10000)

input_path = "data/rosalind_lcsq.txt"
seq_objs = FastaParser(input_path).parse_fasta()
s = [seq_objs[0]["sequence"], seq_objs[1]["sequence"]] # sequences 1 and 2

LCS = [[None for p2 in range(0, len(s[1]))] for p1 in range(0, len(s[0]))]

def get_lcs(s1, s2, p1, p2):
    lcs = ""

    if p1 >= 0 and p2 >= 0:

        # if equal
        if s1[p1] == s2[p2]:
            if LCS[p1-1][p2-1]:
                lcs = LCS[p1-1][p2-1] + s1[p1]

            else:
                lcs = get_lcs(s1, s2, p1 - 1, p2 - 1) + s1[p1]

        # if not equal
        else:
            remove_s1_lcs = ""
            remove_s2_lcs = ""

            if LCS[p1-1][p2]:
                remove_s1_lcs = LCS[p1-1][p2]
            else:
                remove_s1_lcs = get_lcs(s1, s2, p1 - 1, p2)

            if LCS[p1][p2-1]:
                remove_s2_lcs = LCS[p1][p2-1]
            else:
                remove_s2_lcs = get_lcs(s1, s2, p1, p2 - 1)


            if len(remove_s1_lcs) > len(remove_s2_lcs):
                lcs = remove_s1_lcs
            else:
                lcs = remove_s2_lcs

    LCS[p1][p2] = lcs

    return lcs

val = get_lcs(s[0], s[1], len(s[0]) - 1, len(s[1]) - 1)
print(val)
