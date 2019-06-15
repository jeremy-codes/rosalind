"""Solution for Bioinformatics Stronghold Problem ID: MRNA

Problem Title: Inferring mRNA from Protein
Link: http://rosalind.info/problems/mrna
"""

from rosalindutils.constants import DNA_CODON_TABLE as cdn_tbl

# reverse the codon table, so that each aa is the key and the num of different
# codons is the value
all_aas = list(set(cdn_tbl.values()))
aa_codon_count_dict = {aa: 0 for aa in all_aas}

for codon in cdn_tbl.keys():
    aa_codon_count_dict[cdn_tbl[codon]] += 1

total_possibilities = 1

input_path = "data/rosalind_mrna.txt"
aa_seq = open(input_path, "r").read().rstrip()

for i in range(0, len(aa_seq)):
    p = aa_codon_count_dict[aa_seq[i]]
    total_possibilities *= aa_codon_count_dict[aa_seq[i]]

total_possibilities *= aa_codon_count_dict["Stop"]
final_output = total_possibilities % 1000000
print(final_output)
