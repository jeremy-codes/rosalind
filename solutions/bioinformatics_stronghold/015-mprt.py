"""Solution for Bioinformatics Stronghold Problem ID: MPRT

Problem Title: Finding a Protein Motif
Link: http://rosalind.info/problems/mprt
"""

import re
import requests

UNIPROT_URL_TEMPLATE = "http://www.uniprot.org/uniprot/UNIPROTID.fasta"
n_glycosylation_motif = re.compile(r'(?=(N[^P][ST][^P]))')

input_path = "data/rosalind_mprt.txt"
input_file = open(input_path, "r")

final_output = []

for input_line in input_file:
    uniprot_id = input_line.rstrip()
    url = UNIPROT_URL_TEMPLATE.replace("UNIPROTID", uniprot_id)
    response = requests.get(url)
    raw_fasta = response.text

    fasta_l = raw_fasta.split("\n")
    fasta_header = fasta_l[0]
    fasta_seq = "".join(fasta_l[1:])

    match_indices = []

    for motif_match in re.finditer(n_glycosylation_motif, fasta_seq):
        start_pos = motif_match.start() + 1
        match_indices.append(str(start_pos))

    if len(match_indices) > 0:
        final_output.append(uniprot_id + "\n" + " ".join(match_indices))

print("\n".join(final_output))
