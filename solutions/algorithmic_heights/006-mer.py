"""Solution for Algorithmic Heights Problem ID: MER

Problem Title: Merge Two Sorted Arrays
Link: http://rosalind.info/problems/mer
"""

# a: list a
# b: list b
def merge(a, b):
    c = []

    while len(a) > 0 or len(b) > 0:
        new = None

        if len(a) == 0:
            new = b.pop(0)
        elif len(b) == 0:
            new = a.pop(0)
        else:
            if a[0] < b[0]:
                new = a.pop(0)
            else:
                new = b.pop(0)

        c.append(new)

    return c

input_path = "data/rosalind_mer.txt"
output_path = "output/rosalind_mer.output.txt"
input_file = open(input_path, "r")
n = int(input_file.readline().rstrip())
arr_a = [int(a) for a in input_file.readline().rstrip().split(" ")]
m = int(input_file.readline().rstrip())
arr_b = [int(a) for a in input_file.readline().rstrip().split(" ")]

merged = merge(arr_a, arr_b)
open(output_path, "w").write(" ".join([str(x) for x in merged]) + "\n")
