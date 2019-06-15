"""Solution for Python Village Problem ID: INI5

Problem Title: Working with Files
Link: http://rosalind.info/problems/ini5
"""

import math

input_path = "data/rosalind_ini5.txt"
input_file = open(input_path, "r")

output_path = "output/rosalind_ini5.output.txt"
output_file = open(output_path, "w")
output_file.write("")
output_file.close()
output_file = open(output_path, "a")

line_c = 1

for line in input_file:
    if line_c % 2 == 0:
        output_file.write(line)
    line_c += 1

input_file.close()
output_file.close()
