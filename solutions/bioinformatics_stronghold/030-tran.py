"""Solution for Bioinformatics Stronghold Problem ID: TRAN

Problem Title: Transitions and Transversions
Link: http://rosalind.info/problems/tran
"""

from rosalindutils.constants import TRANSITION_TRANVERSION as tstv_tbl
from rosalindutils.fasta_parser import FastaParser

input_path = "data/rosalind_tran.txt"
seq_objs = FastaParser(input_path).parse_fasta()
seq_a = seq_objs[0]["sequence"]
seq_b = seq_objs[1]["sequence"]

tstv_counts_d = {"transition": 0.0, "transversion": 0.0}

for i in range(0, len(seq_a)):
    nuc_a = seq_a[i]
    nuc_b = seq_b[i]

    if nuc_a != nuc_b:
        tstv_counts_d[tstv_tbl[nuc_a + "x" + nuc_b]] += 1.0

ratio = round(tstv_counts_d["transition"] / tstv_counts_d["transversion"], 10)
print(ratio)
