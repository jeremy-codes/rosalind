"""Solution for Bioinformatics Stronghold Problem ID: HAMM

Problem Title: Counting Point Mutations
Link: http://rosalind.info/problems/hamm
"""

seq_a = None
seq_b = None
distance = 0
input_file = "data/rosalind_hamm.txt"

with open(input_file, "r") as infile:
    seq_a = infile.readline().rstrip()
    seq_b = infile.readline().rstrip()

for i in range(0, len(seq_a)):
    if seq_a[i] != seq_b[i]:
        distance += 1

print(distance)
