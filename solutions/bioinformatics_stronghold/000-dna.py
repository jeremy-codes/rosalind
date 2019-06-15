"""Solution for Bioinformatics Stronghold Problem ID: DNA

Problem Title: Counting DNA Nucleotides
Link: http://rosalind.info/problems/dna
"""

dna_counts_dict = {
    "A": 0,
    "C": 0,
    "G": 0,
    "T": 0
}

input_string = open("data/rosalind_dna.txt", "r").read().rstrip()
for i in range(0, len(input_string)):
    letter = input_string[i]
    dna_counts_dict[letter] += 1

print(" ".join([
    str(dna_counts_dict["A"]),
    str(dna_counts_dict["C"]),
    str(dna_counts_dict["G"]),
    str(dna_counts_dict["T"])
]))
