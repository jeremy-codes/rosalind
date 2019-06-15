"""Solution for Bioinformatics Stronghold Problem ID: PERM

Problem Title: Enumerating Gene Orders
Link: http://rosalind.info/problems/perm
"""

permutations = []

def permute(l, s, e):
    # l: list object
    # s: index of item to be swapped
    # e: end index of list

    if s==e: # if the swap index has reached end of string
        permutations.append( " ".join([str(x) for x in l]) )
    else:
        for i in range(s, e+1):
            # swap the swap index with current index, then send recursively
            l[s], l[i] = l[i], l[s]
            permute(l, s+1, e)
            # swap back
            l[s], l[i] = l[i], l[s]

input_path = "data/rosalind_perm.txt"
n = int(open(input_path, "r").read().rstrip())
my_list = [i for i in range(1, n+1)]

permute(my_list, 0, n-1)

print(len(permutations))
print("\n".join(permutations))
