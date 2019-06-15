"""Solution for Bioinformatics Stronghold Problem ID: PMCH

Problem Title: Perfect Matchings and RNA Secondary Structures
Link: http://rosalind.info/problems/pmch
"""

from rosalindutils.functions import permutation_without_replacement as pwor
from rosalindutils.fasta_parser import FastaParser

input_path = "data/rosalind_pmch.txt"
seq_objs = FastaParser(input_path).parse_fasta()
rna_seq = seq_objs[0]["sequence"]

au_pair_count = rna_seq.count("A")
gc_pair_count = rna_seq.count("G")

n_au_perfect_matchings = pwor(au_pair_count, au_pair_count)
n_gc_perfect_matchings = pwor(gc_pair_count, gc_pair_count)
n_au_perfect_matchings = n_au_perfect_matchings * n_gc_perfect_matchings
print(n_au_perfect_matchings)
