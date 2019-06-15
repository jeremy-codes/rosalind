"""Solution for Python Village Problem ID: INI3

Problem Title: Strings and Lists
Link: http://rosalind.info/problems/ini3
"""

import math

input_path = "data/rosalind_ini3.txt"
input_file = open(input_path, "r")
text = input_file.readline().rstrip()
a, b, c, d = [int(x) for x in input_file.readline().rstrip().split(" ")]
input_file.close()

answer = text[a:b+1] + " " + text[c:d+1]
print(answer)
