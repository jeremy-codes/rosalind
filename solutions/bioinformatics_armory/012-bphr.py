"""Solution for Bioinformatics Armory Problem ID: BPHR

Problem Title: Base Quality Distribtion
Link: http://rosalind.info/problems/bphr
"""

from rosalindutils.fastq_parser import FastqParser
from rosalindutils.constants import PHRED_PLUS33_DICT as phred_dict
import re

input_path = "data/rosalind_bphr.txt"
temp_path = "data/rosalind_bphr.temp.fastq"

open(temp_path, "w").write("")
temp_file = open(temp_path, "a")

input_file = open(input_path, "r")
phred_threshold = float(input_file.readline().rstrip())

for line in input_file:
    temp_file.write(line)
temp_file.close()

fastq_reads = FastqParser(temp_path).parse_fastq()
phred_sum_by_position = [0.0 for i in range(0, len(fastq_reads[0].seq))]

for i in range(0, len(fastq_reads[0].seq)):
    for fastq_read in fastq_reads:
        phred_sum_by_position[i] += float(phred_dict[fastq_read.quality[i]])

position_fail_count = 0

for phred_sum in phred_sum_by_position:
    phred_avg = phred_sum / float(len(fastq_reads))
    if phred_avg < phred_threshold:
        position_fail_count += 1

print(position_fail_count)
