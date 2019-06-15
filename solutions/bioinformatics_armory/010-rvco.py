"""Solution for Bioinformatics Armory Problem ID: RVCO

Problem Title: Complementing a Strand of DNA
Link: http://rosalind.info/problems/rvco
"""

from rosalindutils.fasta_parser import FastaParser
from rosalindutils.dna_functions import dna_reverse_complement as revc

input_path = "data/rosalind_rvco.txt"
seqs = FastaParser(input_path).parse_fasta()

palindrome_count = 0

for seq_obj in seqs:
    fwd_seq = seq_obj["sequence"]
    rev_seq = revc(fwd_seq)

    if fwd_seq == rev_seq:
        palindrome_count += 1

print(palindrome_count)
