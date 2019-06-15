"""Solution for Bioinformatics Armory Problem ID: BPHR

Problem Title: Base Quality Distribtion
Link: http://rosalind.info/problems/bphr
"""

from rosalindutils.constants import DNA_CODON_TABLE_U_SUB_T as cdn_tbl
from rosalindutils.dna_functions import dna_reverse_complement as revc

def get_longest_peptide(dna_string):
    longest_peptide = ""

    for dna_i in range(0, len(dna_string)):
        cdn_i = dna_i
        pep_i = 0
        orf_opened = False
        peptide = ""

        cdn = dna_string[cdn_i: cdn_i+3]
        if cdn == "ATG":
            orf_opened = True
            peptide += cdn_tbl[cdn]
            # print("Orf opened at " + str(dna_i))

        while orf_opened:
            cdn_i += 3
            cdn = dna_string[cdn_i: cdn_i+3]

            if len(cdn) < 3:
                orf_opened = False
            else:
                aa = cdn_tbl[cdn]
                if aa == "Stop":
                    orf_opened = False
                else:
                    peptide += aa

        if len(peptide) > len(longest_peptide):
            longest_peptide = peptide

    return longest_peptide

input_path = "data/rosalind_orfr.txt"
input_file = open(input_path, "r")
fwd_dna = input_file.readline().rstrip()
rev_dna = revc(fwd_dna)
input_file.close()

longest_peptide = None
peptide_fwd = get_longest_peptide(fwd_dna)
peptide_rev = get_longest_peptide(rev_dna)

if len(peptide_fwd) > len(peptide_rev):
    longest_peptide = peptide_fwd
else:
    longest_peptide = peptide_rev

print(peptide_rev)
