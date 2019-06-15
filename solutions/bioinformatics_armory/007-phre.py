"""Solution for Bioinformatics Armory Problem ID: PHRE

Problem Title: Read Quality Distribution
Link: http://rosalind.info/problems/phre
"""

from rosalindutils.fastq_parser import FastqParser
from rosalindutils.constants import PHRED_PLUS33_DICT as phred_dict
import re

input_path = "data/rosalind_phre.txt"
temp_path = "data/rosalind_phre.temp.fastq"
open(temp_path, "w").write("")
temp_file = open(temp_path, "a")

input_file = open(input_path, "r")
threshold = float(input_file.readline().rstrip())

for line in input_file:
    temp_file.write(line)
temp_file.close()


fastq_reads = FastqParser(temp_path).parse_fastq()

low_qual_count = 0

for fastq_read in fastq_reads:
    phred_sum = 0

    for phred_score in fastq_read.quality:
        phred_sum += phred_dict[phred_score]

    phred_avg = float(phred_sum) / float(len(fastq_read.quality))
    if phred_avg < threshold:
        low_qual_count += 1

print(low_qual_count)
