"""Solution for Bioinformatics Stronghold Problem ID: CONS

Problem Title: Consensus and Profile
Link: http://rosalind.info/problems/cons
"""

from rosalindutils.fasta_parser import FastaParser

dna_counts = {}

def custom_sort(dna_letter):
    return int(dna_counts[dna_letter])

input_path = "data/rosalind_cons.txt"
seq_objs = FastaParser(input_path).parse_fasta()

consensus_sequence = ""
all_consensus_counts = []

for i in range(0, len(seq_objs[0]["sequence"])):
    dna_letters = ["A", "C", "G", "T"]
    dna_counts = {n: 0 for n in dna_letters}

    for seq_obj in seq_objs:
        nucleotide = seq_obj["sequence"][i]
        dna_counts[nucleotide] += 1

    all_consensus_counts.append(dna_counts)

    sorted_dna_letters = sorted(dna_letters, key=custom_sort)
    consensus_letter = sorted_dna_letters[-1]
    consensus_sequence += consensus_letter

final_output = [consensus_sequence]
for dna_letter in dna_letters:
    output_line = [dna_letter+":"]
    for consensus_count in all_consensus_counts:
        output_line.append(str(consensus_count[dna_letter]))
    output_line = " ".join(output_line)
    final_output.append(output_line)

final_output = "\n".join(final_output)
print(final_output)
