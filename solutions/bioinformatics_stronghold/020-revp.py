"""Solution for Bioinformatics Stronghold Problem ID: REVP

Problem Title: Locating Restriction Sites
Link: http://rosalind.info/problems/revp
"""

import rosalindutils.dna_functions as dnaf
from rosalindutils.fasta_parser import FastaParser

input_path = "data/rosalind_revp.txt"
seq_objs = FastaParser(input_path).parse_fasta()
fwd_seq = seq_objs[0]["sequence"]

seq_l = len(fwd_seq)

for fi in range(0, len(fwd_seq)):
    for pdrome_l in range(4, 13):
        fwd_subseq = fwd_seq[fi: fi + pdrome_l]

        if len(fwd_subseq) == pdrome_l:
            rev_subseq = dnaf.dna_reverse_complement(fwd_subseq)

            if fwd_subseq == rev_subseq:
                pos = fi + 1
                print(str(pos) + " " + str(pdrome_l))
