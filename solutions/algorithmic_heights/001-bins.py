"""Solution for Algorithmic Heights Problem ID: BINS

Problem Title: Binary Search
Link: http://rosalind.info/problems/bins
"""

def midpoint(a, b):
    return int((a + b) / 2)

# l: the list to search
# e: the element to find in the list
def binary_search(l, e):
    ret = -2
    si = 0 # search space start
    ei = len(l) # search space end
    prev_m = None

    match_not_found = True
    search_end_not_reached = True
    while match_not_found and search_end_not_reached:
        m = midpoint(si, ei) # midpoint of search space
        le = l[m] # list element

        if le == e:
            match_not_found = False
            ret = m
        elif le > e:
            ei = m
        elif le < e:
            si = m

        if prev_m == m:
            search_end_not_reached = False

        prev_m = m

    return ret


input_path = "data/rosalind_bins.txt"
output_path = "output/rosalind_bins.output.txt"
input_file = open(input_path, "r")
n = int(input_file.readline().rstrip())
m = int(input_file.readline().rstrip())
arr = [int(a) for a in input_file.readline().rstrip().split(" ")]
tofind_list = [int(a) for a in input_file.readline().rstrip().split(" ")]
input_file.close()

matches = []

for tofind_elem in tofind_list:
    idx = binary_search(arr, tofind_elem) + 1
    matches.append(idx)

open(output_path, "w").write(" ".join([str(m) for m in matches]) + "\n")
