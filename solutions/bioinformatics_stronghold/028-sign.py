"""Solution for Bioinformatics Stronghold Problem ID: SIGN

Problem Title: Enumerating Oriented Gene Orderings
Link: http://rosalind.info/problems/sign
"""

import itertools

input_path = "data/rosalind_sign.txt"
output_path = "output/rosalind_sign.output.txt"
n = int(open(input_path, "r").read().rstrip())

vals = []
signs = [1, -1]

for i in range(1, n+1):
    vals.append(str(i))

vals_perms = list(itertools.permutations(vals))
signs_perms = list(itertools.product(signs, repeat=n))

all_perms = []
for val_perm in vals_perms:
    for sign_perm in signs_perms:
        new_perm = [int(val_perm[i]) * int(sign_perm[i])
                    for i in range(0, len(val_perm))]
        new_perm = " ".join([str(i) for i in new_perm])
        all_perms.append(new_perm)

output = str(len(all_perms)) + "\n" + "\n".join(all_perms) + "\n"
open(output_path, "w").write(output)
