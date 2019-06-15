"""Solution for Bioinformatics Stronghold Problem ID: LCSM

Problem Title: Finding a Shared Motif
Link: http://rosalind.info/problems/lcsm
"""

import re
from rosalindutils.fasta_parser import FastaParser

def get_kmer_length_by_binary_search(lower_bound, upper_bound):
    kmer_length = int(lower_bound) + int((upper_bound - lower_bound) / 2)
    return kmer_length

input_path = "data/rosalind_lcsm.txt"
seq_objs = FastaParser(input_path).parse_fasta()
ref_seq_obj = seq_objs[0]
test_seq_objs = seq_objs[1:]

overall_kmer_length = len(ref_seq_obj["sequence"])
# kmer_length = overall_kmer_length

lower_bound = 1
upper_bound = overall_kmer_length
kmer_length = get_kmer_length_by_binary_search(lower_bound, upper_bound)

common_kmer_not_found = True
largest_common_kmer = ""

while common_kmer_not_found and kmer_length != 0:
    common_kmer_found_for_this_length = False

    for idx in range(0, overall_kmer_length - kmer_length + 1):
        # print("new iteration: " + str(kmer_length) + " " + str(idx) + " " + str(lower_bound) + " " + str(upper_bound))
        ref_kmer = ref_seq_obj["sequence"][idx : idx + kmer_length]
        ref_kmer_pattern = re.compile(ref_kmer)

        found_in_all_tests = True
        for test_seq_obj in test_seq_objs:
            if found_in_all_tests:
                match = ref_kmer_pattern.search(test_seq_obj["sequence"])
                if not match:
                    found_in_all_tests = False

        if found_in_all_tests:
            largest_common_kmer = ref_kmer
            common_kmer_found_for_this_length = True

    if common_kmer_found_for_this_length:
        lower_bound = kmer_length
        # print("new lower bound " + str(lower_bound))
    else:
        upper_bound = kmer_length
        # print("new upper bound " + str(upper_bound))

    kmer_length = get_kmer_length_by_binary_search(lower_bound, upper_bound)

    if upper_bound - lower_bound <= 1:
        common_kmer_not_found = False

print(largest_common_kmer)
