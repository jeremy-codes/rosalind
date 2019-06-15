"""Solution for Bioinformatics Stronghold Problem ID: ORF

Problem Title: Open Reading Frames
Link: http://rosalind.info/problems/orf
"""

from rosalindutils.fasta_parser import FastaParser
from rosalindutils.constants import DNA_CODON_TABLE_U_SUB_T as cdn_tbl
import rosalindutils.dna_functions as dnaf

def translate_all_orfs_per_strand(seq):
    all_peptides = []

    for i in range(0, len(seq)):
        ptl_start_codon = seq[i:i+3]

        # start codon found
        if ptl_start_codon == "ATG":
            stop_codon_not_found = True
            peptide = []

            for orf_i in range(i, len(seq), 3):
                if stop_codon_not_found:
                    codon = seq[orf_i: orf_i+3]
                    if len(codon) == 3:
                        aa = cdn_tbl[codon]
                        if aa == "Stop":
                            stop_codon_not_found = False
                        else:
                            peptide.append(aa)

            if not stop_codon_not_found:
                all_peptides.append("".join(peptide))

    return all_peptides

input_path = "data/rosalind_orf.txt"
seq_objs = FastaParser(input_path).parse_fasta()

seq = seq_objs[0]["sequence"]
seq_revcom = dnaf.dna_reverse_complement(seq)

peptides = translate_all_orfs_per_strand(seq)
peptides_revcom = translate_all_orfs_per_strand(seq_revcom)
peptides_total = list(set(peptides + peptides_revcom))

print("\n".join(peptides_total))
