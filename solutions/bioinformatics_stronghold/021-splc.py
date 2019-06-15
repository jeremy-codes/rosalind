"""Solution for Bioinformatics Stronghold Problem ID: SPLC

Problem Title: RNA Splicing
Link: http://rosalind.info/problems/splc
"""

from rosalindutils.constants import DNA_CODON_TABLE_U_SUB_T as cdn_tbl
from rosalindutils.fasta_parser import FastaParser

input_path = "data/rosalind_splc.txt"
seq_objs = FastaParser(input_path).parse_fasta()

template_seq = seq_objs[0]["sequence"]
intron_seqs = [s["sequence"] for s in seq_objs[1:]]

# splice out introns
for intron_seq in intron_seqs:
    template_seq = template_seq.replace(intron_seq, "")

orf_not_found = True
aa_seq = ""
for i in range(0, len(template_seq)):
    if orf_not_found:
        ptl_codon = template_seq[i: i+3]
        if len(ptl_codon) == 3:

            if ptl_codon == "ATG":
                stop_codon_not_found = True
                for a in range(i, len(template_seq), 3):
                    if stop_codon_not_found:
                        codon = template_seq[a: a+3]
                        if len(codon) == 3:
                            aa = cdn_tbl[codon]

                            if aa == "Stop":
                                stop_codon_not_found = False
                                orf_not_found = False
                            else:
                                aa_seq += aa

print(aa_seq)
