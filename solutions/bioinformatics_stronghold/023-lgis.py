"""Solution for Bioinformatics Stronghold Problem ID: LGIS

Problem Title: Longest Increasing Subsequence
Link: http://rosalind.info/problems/lgis
"""

input_path = "data/rosalind_lgis.txt"
input_file = open(input_path, "r")
n = int(input_file.readline().rstrip())
nums = [int(a) for a in input_file.readline().rstrip().split(" ")]
input_file.close()

output_path = "output/rosalind_lgis.output.txt"
open(output_path, "w").write("")
output_file = open(output_path, "a")

# TEST
# nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13]
# nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# nums = [15, 27, 14, 38, 63, 55, 46, 65, 85]

# longest increasing subsequence
# takes the overall sequence, and the current position to be evaluated

subseqs = [] # holds all potential subseqs

for a in range(0, len(nums)):
    num = nums[a]

    case_0 = False
    case_1 = False
    case_2 = False
    case_3 = False

    subseq_count = 0
    num_greater_than_end_element = []
    num_less_than_end_element = []

    for subseq_idx in range(0, len(subseqs)):
        subseq = subseqs[subseq_idx]
        subseq_count += 1
        if num < subseq[-1]:
            num_less_than_end_element.append(subseq_idx)
        if num > subseq[-1]:
            num_greater_than_end_element.append(subseq_idx)

    if subseq_count == 0:
        case_0 = True
    elif len(num_less_than_end_element) > 0 and len(num_greater_than_end_element) == 0:
        case_1 = True
    elif len(num_greater_than_end_element) > 0 and len(num_less_than_end_element) == 0:
        case_2 = True
    elif len(num_greater_than_end_element) > 0 and len(num_less_than_end_element) > 0:
        case_3 = True

    # case 0: no elements in subseq list, start new subseq
    if case_0:
        # print("case 0")
        new_candidate = [num]
        subseqs.append(new_candidate)
    # case 1: if num is the smallest among all candidates, start new active
    # list of length 1
    elif case_1:
        # print("case 1")
        new_candidate = [num]
        subseqs.append(new_candidate)
    # case 2: if num is largest among all end candidates of active lists,
    # clone the largest and extend
    elif case_2:
        # print("case 2")
        longest_list = []
        longest_len = 0

        for sidx in num_greater_than_end_element:
            if len(subseqs[sidx]) > longest_len:
                longest_len = len(subseqs[sidx])
                longest_list = subseqs[sidx]

        new_list = [a for a in longest_list] + [num]
        subseqs.append(new_list)
    # case 3: if num is in between, find a list with largest end element
    # smaller than num. Clone and extend this list by num
    elif case_3:
        # print("case 3")
        largest_end_element_smaller_than_num = -1
        largest_end_element_smaller_than_num_list = None

        for sidx in num_greater_than_end_element:
            if subseqs[sidx][-1] > largest_end_element_smaller_than_num:
                largest_end_element_smaller_than_num = subseqs[sidx][-1]
                largest_end_element_smaller_than_num_list = subseqs[sidx]

        new_list = [a for a in largest_end_element_smaller_than_num_list] + [num]
        subseqs.append(new_list)

        # for each subsequence length, the best subsequence has the lowest
        # end number, therefore for each subsequence length, choose only the
        # best subsequence
        reoptimized_subseqs = []
        subseqs_by_len = {}

        for subseq in subseqs:
            if len(subseq) not in subseqs_by_len.keys():
                subseqs_by_len[len(subseq)] = []
            subseqs_by_len[len(subseq)].append(subseq)

        for key in subseqs_by_len.keys():
            lowest_last_num = 100000
            lowest_last_num_subseq = None

            for subseq in subseqs_by_len[key]:
                if subseq[-1] < lowest_last_num:
                    lowest_last_num = subseq[-1]
                    lowest_last_num_subseq = subseq

            reoptimized_subseqs.append(lowest_last_num_subseq)

        subseqs = reoptimized_subseqs

final_longest = []
final_longest_len = 0
for subseq in subseqs:
    if len(subseq) > final_longest_len:
        final_longest_len = len(subseq)
        final_longest = subseq

output_file.write(" ".join([str(a) for a in final_longest]) + "\n")

# LONGEST DECREASING SUBSEQUENCE
# takes the overall sequence, and the current position to be evaluated

subseqs = [] # holds all potential subseqs

for a in range(0, len(nums)):
    num = nums[a]

    case_0 = False
    case_1 = False
    case_2 = False
    case_3 = False

    subseq_count = 0
    num_greater_than_end_element = []
    num_less_than_end_element = []

    for subseq_idx in range(0, len(subseqs)):
        subseq = subseqs[subseq_idx]
        subseq_count += 1
        if num < subseq[-1]:
            num_less_than_end_element.append(subseq_idx)
        if num > subseq[-1]:
            num_greater_than_end_element.append(subseq_idx)

    if subseq_count == 0:
        case_0 = True
    elif len(num_greater_than_end_element) > 0 and len(num_less_than_end_element) == 0:
        case_1 = True
    elif len(num_less_than_end_element) > 0 and len(num_greater_than_end_element) == 0:
        case_2 = True
    elif len(num_greater_than_end_element) > 0 and len(num_less_than_end_element) > 0:
        case_3 = True

    # case 0: no elements in subseq list, start new subseq
    if case_0:
        # print("case 0")
        new_candidate = [num]
        subseqs.append(new_candidate)
    # case 1: if num is the largest among all candidates, start new active
    # list of length 1
    elif case_1:
        # print("case 1")
        new_candidate = [num]
        subseqs.append(new_candidate)
    # case 2: if num is smallest among all end candidates of active lists,
    # clone the longest and extend
    elif case_2:
        # print("case 2")
        longest_list = []
        longest_len = 0

        for sidx in num_less_than_end_element:
            if len(subseqs[sidx]) > longest_len:
                longest_len = len(subseqs[sidx])
                longest_list = subseqs[sidx]

        new_list = [a for a in longest_list] + [num]
        subseqs.append(new_list)

    # case 3: if num is in between, find a list with smallest end element
    # larger than num. Clone and extend this list by num
    elif case_3:
        # print("case 3")
        smallest_end_element_larger_than_num = 100000
        smallest_end_element_larger_than_num_list = None

        for sidx in num_less_than_end_element:
            if subseqs[sidx][-1] < smallest_end_element_larger_than_num:
                smallest_end_element_larger_than_num = subseqs[sidx][-1]
                smallest_end_element_larger_than_num_list = subseqs[sidx]

        new_list = [a for a in smallest_end_element_larger_than_num_list] + [num]
        subseqs.append(new_list)

        # for each subsequence length, the best subsequence has the lowest
        # end number, therefore for each subsequence length, choose only the
        # best subsequence
        reoptimized_subseqs = []
        subseqs_by_len = {}

        for subseq in subseqs:
            if len(subseq) not in subseqs_by_len.keys():
                subseqs_by_len[len(subseq)] = []
            subseqs_by_len[len(subseq)].append(subseq)

        for key in subseqs_by_len.keys():
            highest_last_num = -1
            highest_last_num_subseq = None

            for subseq in subseqs_by_len[key]:
                if subseq[-1] > highest_last_num:
                    highest_last_num = subseq[-1]
                    highest_last_num_subseq = subseq

            reoptimized_subseqs.append(highest_last_num_subseq)

        subseqs = reoptimized_subseqs

final_longest = []
final_longest_len = 0
for subseq in subseqs:
    if len(subseq) > final_longest_len:
        final_longest_len = len(subseq)
        final_longest = subseq

output_file.write(" ".join([str(a) for a in final_longest]) + "\n")
