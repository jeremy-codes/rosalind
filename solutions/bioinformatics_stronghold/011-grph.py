"""Solution for Bioinformatics Stronghold Problem ID: GRPH

Problem Title: Overlap Graphs
Link: http://rosalind.info/problems/grph
"""

from rosalindutils.fasta_parser import FastaParser

input_path = "data/rosalind_grph.txt"
output_path = "output/rosalind_grph.output.txt"
seq_objs = FastaParser(input_path).parse_fasta()

edge_relationships = []

for seq_obj_a in seq_objs:
    head_a = seq_obj_a["header"]
    seq_a = seq_obj_a["sequence"]

    for seq_obj_b in seq_objs:
        head_b = seq_obj_b["header"]
        seq_b = seq_obj_b["sequence"]

        if head_a != head_b and seq_a != seq_b:
            a_suffix = seq_a[-3:]
            b_prefix = seq_b[0:3]
            if a_suffix == b_prefix:
                edge_relationship = head_a + " " + head_b
                edge_relationships.append(edge_relationship)

open(output_path, "w").write("\n".join(edge_relationships) + "\n")
