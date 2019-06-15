"""Solution for Bioinformatics Stronghold Problem ID: GC

Problem Title: Computing GC Content
Link: http://rosalind.info/problems/gc
"""

def parse_fasta(input_file):

    sequence_obj = {"header": None, "sequence": ""}
    all_sequence_objs = []

    with open(input_file, "r") as infile:
        sequence_obj["header"] = infile.readline().rstrip()[1:]

        for line in infile:
            lr = line.rstrip()

            if (lr.startswith(">")):
                all_sequence_objs.append(sequence_obj)
                sequence_obj = {"header": lr[1:], "sequence": ""}
            else:
                sequence_obj["sequence"] += lr

        all_sequence_objs.append(sequence_obj)

    return all_sequence_objs

def compute_gc(sequence_obj):
    gc_count = sequence_obj["sequence"].count("C") \
               + sequence_obj["sequence"].count("G")
    seq_length = len(sequence_obj["sequence"])
    gc_content = float(gc_count) / float(seq_length)
    gc_percent = round(gc_content * 100.0, 6)
    return gc_percent

input_file = "data/rosalind_gc.txt"
sequences_list = parse_fasta(input_file)

highest_gc_header = None
highest_gc_content = 0.0

for sequence_obj in sequences_list:
    gc_content = compute_gc(sequence_obj)
    if gc_content > highest_gc_content:
        highest_gc_header = sequence_obj["header"]
        highest_gc_content = gc_content

print(highest_gc_header + "\n" + str(highest_gc_content))
