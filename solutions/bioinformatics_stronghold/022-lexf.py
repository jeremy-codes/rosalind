"""Solution for Bioinformatics Stronghold Problem ID: LEXF

Problem Title: Enumerating k-mers Lexicographically
Link: http://rosalind.info/problems/lexf
"""

import itertools

permutations = []

input_path = "data/rosalind_lexf.txt"
output_path = "output/rosalind_lexf.output.txt"

input_file = open(input_path, "r")
letters_l = input_file.readline().rstrip().split(" ")
kmer_length = int(input_file.readline().rstrip())
input_file.close()

unsorted_tuples = list(itertools.product(letters_l, repeat=kmer_length))
unsorted_strings = ["".join(t) for t in unsorted_tuples]
sorted_strings = sorted(unsorted_strings)

open(output_path, "w").write("\n".join(sorted_strings) + "\n")
