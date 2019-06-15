"""Solution for Bioinformatics Armory Problem ID: INI

Problem Title: Introduction to the Bioinformatics Armory
Link: http://rosalind.info/problems/ini
"""

input_path = "data/rosalind_ini.txt"
input_file = open(input_path, "r")
dna_string = input_file.readline().rstrip()

dna_letters = ["A", "C", "G", "T"]
dna_counts = {l: 0 for l in dna_letters}

for l in dna_string:
    dna_counts[l] += 1

print(" ".join([str(dna_counts[l]) for l in dna_letters]))
