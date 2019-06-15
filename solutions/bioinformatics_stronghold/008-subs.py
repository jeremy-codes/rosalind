"""Solution for Bioinformatics Stronghold Problem ID: SUBS

Problem Title: Finding a Motif in DNA
Link: http://rosalind.info/problems/subs
"""

input_path = "data/rosalind_subs.txt"
input_file = open(input_path, "r")

dna_strand = input_file.readline().rstrip()
motif = input_file.readline().rstrip()
lookahead = len(motif)

hits = []

for i in range(0, len(dna_strand)):
    hit_index = i + 1
    potential_motif = dna_strand[i:i + lookahead]
    if potential_motif == motif:
        hits.append(hit_index)

hits_string = " ".join([str(hit) for hit in hits])
print(hits_string)
