"""Solution for Bioinformatics Armory Problem ID: TFSQ

Problem Title: FASTQ format introduction
Link: http://rosalind.info/problems/tfsq
"""

import re

def parse_fastq(input_path):
    input_file = open(input_path, "r")
    all_reads = []
    all_lines_in_read = []

    for line in input_file:
        if len(all_lines_in_read) == 4:
            all_reads.append(all_lines_in_read)
            all_lines_in_read = []

        all_lines_in_read.append(line)

    all_reads.append(all_lines_in_read)

    return all_reads

def convert_fastq_to_fasta(read):
    new_header = re.sub("^@", ">", read[0])
    new_seq = read[1]

    return new_header + new_seq

input_path = "data/rosalind_tfsq.txt"
output_path = "output/rosalind_tfsq.output.txt"
all_reads = parse_fastq(input_path)
all_fasta = []

for read in all_reads:
    fasta_read = convert_fastq_to_fasta(read)
    all_fasta.append(fasta_read)

open(output_path, "w").write("\n".join(all_fasta) + "\n")
