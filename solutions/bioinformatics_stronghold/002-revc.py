"""Solution for Bioinformatics Stronghold Problem ID: REVC

Problem Title: Complementing a String of DNA
Link: http://rosalind.info/problems/revc
"""

revcom_dict = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

input_strand = open("data/rosalind_revc.txt", "r").read().rstrip()
reverse_strand = input_strand[::-1]
revcom_strand = ""

for i in range(0, len(reverse_strand)):
    revcom_strand += revcom_dict[reverse_strand[i]]

print(revcom_strand)
