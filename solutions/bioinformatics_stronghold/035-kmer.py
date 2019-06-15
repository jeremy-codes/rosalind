"""Solution for Bioinformatics Stronghold Problem ID: KMER

Problem Title: k-Mer Composition
Link: http://rosalind.info/problems/kmer
"""

import itertools
from rosalindutils.fasta_parser import FastaParser

input_path = "data/rosalind_kmer.txt"
seq_objs = FastaParser(input_path).parse_fasta()
seq = seq_objs[0]["sequence"]

dna_letters = ["A", "C", "G", "T"]

kmers_4 = list(itertools.product(dna_letters, repeat=4))
kmers_4 = ["".join(k) for k in kmers_4]
kmer_counts_d = {k: 0 for k in kmers_4}

for i in range(0, len(seq) - 3):
    subseq = seq[i:i+4]
    kmer_counts_d[subseq] += 1

print( " ".join([str(kmer_counts_d[kmer]) for kmer in kmers_4]) )
