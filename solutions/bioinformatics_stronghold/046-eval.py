"""Solution for Bioinformatics Stronghold Problem ID: EVAL

Problem Title: Expected Number of Restriction Sites
Link: http://rosalind.info/problems/eval
"""

input_path = "data/rosalind_eval.txt"
input_file = open(input_path, "r")
n = int(input_file.readline().rstrip())
subseq = input_file.readline().rstrip()
gc_list = input_file.readline().rstrip().split(" ")

occurrences_list = []

for gc_content in gc_list:
    gc = float(gc_content)
    g_or_c = gc / 2.0
    a_or_t = (1.0 - gc) / 2.0
    base_probs = {"A": a_or_t, "T": a_or_t, "C": g_or_c, "G": g_or_c}

    subseq_prob = 1.0
    for i in range(0, len(subseq)):
        subseq_prob *= base_probs[subseq[i]]

    n_chances = n - len(subseq) + 1
    n_occurrences = subseq_prob * n_chances
    occurrences_list.append(str(round(n_occurrences, 5)))

print(" ".join(occurrences_list))
