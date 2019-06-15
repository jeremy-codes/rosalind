"""Solution for Bioinformatics Stronghold Problem ID: INOD

Problem Title: Counting Phylogenetic Ancestors
Link: http://rosalind.info/problems/inod
"""

input_path = "data/rosalind_inod.txt"
input_file = open(input_path, "r")
n_leaves = int(input_file.read().rstrip())
n_internal_nodes = n_leaves - 2
print(n_internal_nodes)
