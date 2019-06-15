"""Solution for Bioinformatics Stronghold Problem ID: SPEC

Problem Title: Inferring Protein from Spectrum
Link: http://rosalind.info/problems/spec
"""

from rosalindutils.constants import MONOISOTOPIC_MASS_TABLE as mass_tbl

mass_to_aa = {str(round(mass_tbl[k], 5)): k for k in mass_tbl.keys()}

input_path = "data/rosalind_spec.txt"
input_file = open(input_path, "r")
all_masses = []

for l in input_file:
    all_masses.append(float(l.rstrip()))

sorted_masses = sorted(all_masses)
peptide = ""

for i in range(1, len(sorted_masses)):
    mass_diff = round(sorted_masses[i] - sorted_masses[i-1], 5)
    aa = mass_to_aa[str(mass_diff)]
    peptide += aa

print(peptide)
