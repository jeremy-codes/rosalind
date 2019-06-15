"""Solution for Python Village Problem ID: INI6

Problem Title: Dictionaries
Link: http://rosalind.info/problems/ini6
"""

import math

input_path = "data/rosalind_ini6.txt"
input_file = open(input_path, "r")
text = input_file.readline().rstrip()
input_file.close()
text_l = text.split(" ")

word_dict = {}

for word in text_l:
    if word not in word_dict.keys():
        word_dict[word] = 0
    word_dict[word] += 1

for word in word_dict.keys():
    print(word + " " + str(word_dict[word]))
