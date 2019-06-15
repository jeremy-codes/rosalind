"""Solution for Bioinformatics Stronghold Problem ID: PDST

Problem Title: Creating a Distance Matrix
Link: http://rosalind.info/problems/pdst
"""

import itertools
from rosalindutils.fasta_parser import FastaParser

input_path = "data/rosalind_pdst.txt"
seq_objs = FastaParser(input_path).parse_fasta()

dna_letters = ["A", "C", "G", "T"]
hamm_values = {}
hamm_values_no_change = {l+l: 0.0 for l in dna_letters}

changes_l = ["".join(p) for p in list(itertools.permutations(dna_letters, 2))]
hamm_values_change = {c: 1.0 for c in changes_l}

hamm_values.update(hamm_values_no_change)
hamm_values.update(hamm_values_change)

pairwise_hamm_counts_l = []

for a in range(0, len(seq_objs)):
    seq_a = seq_objs[a]["sequence"]
    hamm_vals_for_seq_a = []

    for b in range(0, len(seq_objs)):
        seq_b = seq_objs[b]["sequence"]
        hamm = 0.0

        for i in range(0, len(seq_a)):
            hamm += hamm_values[seq_a[i] + seq_b[i]]

        hamm_ratio = round(hamm / float(len(seq_a)), 5)
        hamm_vals_for_seq_a.append(str(hamm_ratio))

    pairwise_hamm_counts_l.append(" ".join(hamm_vals_for_seq_a))

print("\n".join(pairwise_hamm_counts_l))
