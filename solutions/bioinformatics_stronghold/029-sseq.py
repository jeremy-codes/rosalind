"""Solution for Bioinformatics Stronghold Problem ID: SSEQ

Problem Title: Finding a Spliced Motif
Link: http://rosalind.info/problems/sseq
"""

from rosalindutils.fasta_parser import FastaParser

input_path = "data/rosalind_sseq.txt"
seq_objs = FastaParser(input_path).parse_fasta()

seq = seq_objs[0]["sequence"]
motif = seq_objs[1]["sequence"]

seq_motif_positions = []
motif_idx = 0
motif_incomplete = True

for s in range(0, len(seq)):
    if motif_incomplete:
        if seq[s] == motif[motif_idx]:
            seq_motif_positions.append(str(s + 1))
            motif_idx += 1

            if motif_idx == len(motif):
                motif_incomplete = False

print(" ".join(seq_motif_positions))
