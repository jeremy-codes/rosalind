"""Solution for Python Village Problem ID: INI2

Problem Title: Variables and Some Arithmetic
Link: http://rosalind.info/problems/ini2
"""

import math

input_path = "data/rosalind_ini2.txt"
input_file = open(input_path, "r")
a, b = input_file.readline().rstrip().split(" ")
a, b = [int(x) for x in [a, b]]
input_file.close()

answer = int( math.pow(a, 2) + math.pow(b, 2) )
print(answer)
