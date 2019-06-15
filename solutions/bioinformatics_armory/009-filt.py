"""Solution for Bioinformatics Armory Problem ID: FILT

Problem Title: Read Filtration by Quality
Link: http://rosalind.info/problems/filt
"""

from rosalindutils.fastq_parser import FastqParser
from rosalindutils.constants import PHRED_PLUS33_DICT as phred_dict
import re

input_path = "data/rosalind_filt.txt"
temp_path = "data/rosalind_filt.temp.fastq"
open(temp_path, "w").write("")
temp_file = open(temp_path, "a")

input_file = open(input_path, "r")
threshold, req_percent = [float(x)
                          for x in input_file.readline().rstrip().split(" ")]

for line in input_file:
    temp_file.write(line)
temp_file.close()

fastq_reads = FastqParser(temp_path).parse_fastq()

read_pass_count = 0

for fastq_read in fastq_reads:
    base_pass_count = 0

    for phred_symbol in fastq_read.quality:
        phred_score = phred_dict[phred_symbol]
        if phred_score >= threshold:
            base_pass_count += 1

    percent_pass = 100.0 * (float(base_pass_count) /
                            float(len(fastq_read.quality)))

    if percent_pass >= req_percent:
        read_pass_count += 1

print(read_pass_count)
