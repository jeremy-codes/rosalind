"""Solution for Python Village Problem ID: INI4

Problem Title: Conditions and Loops
Link: http://rosalind.info/problems/ini4
"""

import math

input_path = "data/rosalind_ini4.txt"
input_file = open(input_path, "r")
a, b = [int(x) for x in input_file.readline().rstrip().split(" ")]
input_file.close()

answer = 0

for i in range(a, b+1):
    if i % 2 == 1:
        answer += i

print(answer)
