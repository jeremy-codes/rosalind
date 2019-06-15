"""Solution for Bioinformatics Stronghold Problem ID: PRTM

Problem Title: Calculating Mass
Link: http://rosalind.info/problems/prtm
"""

from rosalindutils.constants import MONOISOTOPIC_MASS_TABLE as mass_tbl

mass_total = 0.0

input_path = "data/rosalind_prtm.txt"
aa_seq = open(input_path, "r").read().rstrip()

for aa in aa_seq:
    mass_total += mass_tbl[aa]

print(round(mass_total, 5))
