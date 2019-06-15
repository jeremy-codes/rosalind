"""Solution for Algorithmic Heights Problem ID: INS

Problem Title: Insertion Sort
Link: http://rosalind.info/problems/ins
"""

def insertion_sort(arr):
    n_changes = 0
    changes_made = True

    while changes_made:
        n_changes_this_cycle = 0

        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                n_changes_this_cycle += 1
                n_changes += 1

        if n_changes_this_cycle == 0:
            changes_made = False

    return n_changes


input_path = "data/rosalind_ins.txt"
input_file = open(input_path, "r")
n = int(input_file.readline().rstrip())
nums = [int(a) for a in input_file.readline().rstrip().split(" ")]
n_changes = insertion_sort(nums)
print(n_changes)
