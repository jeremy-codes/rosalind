"""Solution for Bioinformatics Stronghold Problem ID: SSET

Problem Title: Counting Subsets
Link: http://rosalind.info/problems/sset
"""

from rosalindutils.functions import combination_without_replacement as cwor

input_path = "data/rosalind_sset.txt"
n = int(open(input_path, "r").read().rstrip())

total_mod_million = 0.0

for r in range(0, n+1):
    subtotal = cwor(n, r)
    subtotal_mod_million = subtotal % 1000000.0

    total_mod_million += subtotal_mod_million
    total_mod_million = total_mod_million % 1000000.0

print(total_mod_million)
