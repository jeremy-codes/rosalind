"""Solution for Bioinformatics Armory Problem ID: PTRA

Problem Title: Protein Translation
Link: http://rosalind.info/problems/ptra
"""

from rosalindutils.constants import DNA_CODON_TABLE_U_SUB_T as cdn_tbl

input_path = "data/rosalind_ptra.txt"
input_file = open(input_path, "r")
dna_string = input_file.readline().rstrip()
peptide_string = input_file.readline().rstrip()
input_file.close()

final_match_idx = None

for dna_i in range(0, len(dna_string)):
    cdn_i = dna_i
    pep_i = 0
    peptide_match = True

    while peptide_match and not final_match_idx:
        cdn = dna_string[cdn_i: cdn_i+3]
        true_aa = None
        if pep_i == len(peptide_string):
            true_aa = "Stop"
        else:
            true_aa = peptide_string[pep_i]
        test_aa = cdn_tbl[cdn]

        if true_aa == test_aa:
            cdn_i += 3
            pep_i += 1
            if true_aa == "Stop":
                final_match_idx = dna_i + 1
        else:
            peptide_match = False

print(final_match_idx)
