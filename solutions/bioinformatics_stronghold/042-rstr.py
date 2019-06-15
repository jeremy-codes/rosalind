"""Solution for Bioinformatics Stronghold Problem ID: RSTR

Problem Title: Matching Random Motifs
Link: http://rosalind.info/problems/rstr
"""

import math

input_path = "data/rosalind_rstr.txt"
input_file = open(input_path, "r")
n_seq, gc_content = input_file.readline().rstrip().split(" ")
seq = input_file.readline().rstrip()

n_seq = int(n_seq)
gc_content = float(gc_content)

g_or_c_chance = gc_content / 2.0
a_or_t_chance = (1.0 - gc_content) / 2.0
base_chance_d = {
    "A": a_or_t_chance, "T": a_or_t_chance,
    "G": g_or_c_chance, "C": g_or_c_chance
}

# get the chance that a random sequence will be the target based on
# provided gc content
seq_chance = 1.0
for i in range(0, len(seq)):
    seq_chance *= base_chance_d[seq[i]]

# the probability of any other sequence
not_seq_chance = 1.0 - seq_chance

# now, what is the probability we get 0 target sequences for all N sequences?
no_sequences_chance = math.pow(not_seq_chance, n_seq)

# the probability we get any (1 or more) target sequences is:
# 1 - the probability we get 0 sequences for all n sequences
any_target_sequences_change = 1.0 - no_sequences_chance
print(round(any_target_sequences_change, 3))
