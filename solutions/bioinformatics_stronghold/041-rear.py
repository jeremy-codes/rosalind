"""Solution for Bioinformatics Stronghold Problem ID: REAR

Problem Title: Reversal Distance
Link: http://rosalind.info/problems/rear
"""

input_path = "data/rosalind_rear.txt"
input_file = open(input_path, "r")
permutation_pairs = input_file.read().rstrip().split("\n\n")

for pair in permutation_pairs:
    template, perm = [e.split(" ") for e in pair.split("\n")]
    reverse_count = 0

    # print(template)
    # print("---")

    for i in range(0, len(template)):

        # print(str(perm) + "\t" + str(reverse_count))

        if template[i] != perm[i]:
            reverse_count += 1
            swap_start_idx = i
            swap_end_idx = None

            for s in range(i, len(perm)):
                if not swap_end_idx:
                    if template[i] == perm[s]:
                        swap_end_idx = s

            swap = True
            while swap:
                if swap_start_idx >= swap_end_idx:
                    swap = False
                else:
                    perm[swap_start_idx], perm[swap_end_idx] = \
                    perm[swap_end_idx], perm[swap_start_idx]
                    swap_start_idx += 1
                    swap_end_idx -= 1

            # print(perm)

    print(reverse_count)
