"""Solution for Bioinformatics Stronghold Problem ID: LEXV

Problem Title: Ordering Strings of Varying Length Lexicographically
Link: http://rosalind.info/problems/lexv
"""

import itertools

input_path = "data/rosalind_lexv.txt"
output_path = "output/rosalind_lexv.output.txt"

input_file = open(input_path, "r")
letters = input_file.readline().rstrip().split(" ")
max_n = int(input_file.readline().rstrip())
input_file.close()

all_permutations = []
for n in range(1, max_n + 1):
    permutations = list(itertools.product(letters, repeat=n))
    permutations = ["".join(p) for p in permutations]
    all_permutations += permutations

sorted_all_permutations = sorted(
    all_permutations,
    key=lambda word: [letters.index(c) for c in word]
)
open(output_path, "w").write("\n".join(sorted_all_permutations) + "\n")
