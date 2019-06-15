"""Solution for Bioinformatics Armory Problem ID: FRMT

Problem Title: Data Formats
Link: http://rosalind.info/problems/frmt
"""

from Bio import Entrez
from Bio import SeqIO

input_path = "data/rosalind_frmt.txt"
input_file = open(input_path, "r")
accessions_l = input_file.readline().rstrip().split(" ")

Entrez.email = "jeremybr.adams@gmail.com"
handle_a = Entrez.efetch(db="nucleotide", rettype="fasta",
                         id=["%s" % (", ".join(accessions_l))])
handle_b = Entrez.efetch(db="nucleotide", rettype="fasta",
                         id=["%s" % (", ".join(accessions_l))])

records = list(SeqIO.parse(handle_a, "fasta"))
records_orig = handle_b.read().split("\n\n")[:-1]

shortest_length = float("inf")
shortest_idx = None

i = 0
for record in records:

    if len(record.seq) < shortest_length:
        shortest_idx = i
        shortest_length = len(record.seq)

    i += 1

print(records_orig[shortest_idx])
