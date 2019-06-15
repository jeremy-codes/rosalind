"""Solution for Bioinformatics Stronghold Problem ID: CORR

Problem Title: Error Correction in Reads
Link: http://rosalind.info/problems/corr
"""

def common_bases(seq_a, seq_b):
    common = 0
    for i in range(0, len(seq_a)):
        if seq_a[i] == seq_b[i]:
            common += 1
    return common

from rosalindutils.fasta_parser import FastaParser
from rosalindutils.dna_functions import dna_reverse_complement as revcom

input_path = "data/rosalind_corr.txt"
output_path = "output/rosalind_corr.output.txt"
seqs = FastaParser(input_path).parse_fasta()
seq_counts = {}

for s in range(0, len(seqs)):
    fwd_s = seqs[s]["sequence"]
    rev_s = revcom(fwd_s)

    if fwd_s not in seq_counts.keys() and rev_s not in seq_counts.keys():
        seq_counts[fwd_s] = 1
    elif fwd_s in seq_counts.keys():
        seq_counts[fwd_s] += 1
    elif rev_s in seq_counts.keys():
        seq_counts[rev_s] += 1

corr_reads = [seq for seq in seq_counts.keys() if seq_counts[seq] > 1]
incorr_reads = [seq for seq in seq_counts.keys() if seq_counts[seq] == 1]

corrections = []

for incorr_read in incorr_reads:

    fwd_read = incorr_read
    rev_read = revcom(fwd_read)
    match_read_not_found = True

    for corr_read in corr_reads:
        if match_read_not_found:
            fwd_common = common_bases(fwd_read, corr_read)
            rev_common = common_bases(rev_read, corr_read)

            if fwd_common == len(fwd_read) - 1:
                correction = fwd_read + "->" + corr_read
                corrections.append(correction)
                match_read_not_found = False

            elif rev_common == len(rev_read) -1:
                correction = rev_read + "->" + corr_read
                corrections.append(correction)
                match_read_not_found = False

open(output_path, "w").write("\n".join(corrections) + "\n")
