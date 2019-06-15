"""Solution for Bioinformatics Stronghold Problem ID: RNA

Problem Title: Transcribing DNA into RNA
Link: http://rosalind.info/problems/rna
"""

input_string = open("data/rosalind_rna.txt", "r").read().rstrip()
output_string = input_string.replace("T", "U")
print(output_string)
