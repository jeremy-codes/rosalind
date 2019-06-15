"""Solution for Bioinformatics Armory Problem ID: BFIL

Problem Title: Base Filtration by Quality
Link: http://rosalind.info/problems/bfil
"""

from rosalindutils.fastq_parser import FastqParser
from rosalindutils.constants import PHRED_PLUS33_DICT as phred_dict
import re

input_path = "data/rosalind_bfil.txt"
output_path = "output/rosalind_bfil.output.txt"
temp_path = "data/rosalind_bfil.temp.fastq"

open(temp_path, "w").write("")
temp_file = open(temp_path, "a")

input_file = open(input_path, "r")
phred_threshold = float(input_file.readline().rstrip())

for line in input_file:
    temp_file.write(line)
temp_file.close()

fastq_reads = FastqParser(temp_path).parse_fastq()
trimmed_reads = []

for fastq_read in fastq_reads:
    start_idx = 0
    end_idx = len(fastq_read.seq) - 1

    # how many to trim from start
    start_not_found = True
    for s in range(0, len(fastq_read.seq)):
        if start_not_found:
            phred_score = float(phred_dict[fastq_read.quality[s]])
            if phred_score >= phred_threshold:
                start_idx = s
                start_not_found = False

    # how many to trime from end
    end_not_found = True
    for e in range(len(fastq_read.seq) - 1, 0, -1):
        if end_not_found:
            phred_score = float(phred_dict[fastq_read.quality[e]])
            if phred_score >= phred_threshold:
                end_idx = e
                end_not_found = False

    trimmed_read = fastq_read.header + "\n" \
                   + fastq_read.seq[start_idx: end_idx + 1] + "\n" \
                   + fastq_read.spacer + "\n" \
                   + fastq_read.quality[start_idx: end_idx + 1] + "\n"

    trimmed_reads.append(trimmed_read)

open(output_path, "w").write("".join(trimmed_reads) + "\n")
