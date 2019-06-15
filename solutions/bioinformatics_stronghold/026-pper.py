"""Solution for Bioinformatics Stronghold Problem ID: PPER

Problem Title: Partial Permutations
Link: http://rosalind.info/problems/pper
"""

from rosalindutils.functions import permutation_without_replacement as pwor

input_path = "data/rosalind_pper.txt"
input = open(input_path, "r").read().rstrip().split(" ")

n = int(input[0])
k = int(input[1])
perm = pwor(n, k)
final = perm % 1000000
print(final)
