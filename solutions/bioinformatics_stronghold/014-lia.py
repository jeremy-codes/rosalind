"""Solution for Bioinformatics Stronghold Problem ID: LIA

Problem Title: Independent Alleles
Link: http://rosalind.info/problems/lia
"""

import math
from rosalindutils.functions import combination_without_replacement
from rosalindutils.constants import OFFSPRING_GENOTYPE_TABLE as OGT

input_path = "data/rosalind_lia.txt"
input = open(input_path, "r").read().rstrip().split(" ")

kGenerations = int(input[0])
nThreshold = int(input[1])

all_genotypes = [
    "AA BB", "AA Bb", "AA bb",
    "Aa BB", "Aa Bb", "Aa bb",
    "aa BB", "aa Bb", "aa bb"
]

mate_genotype = "Aa Bb"

genotype_per_generation = [
    {"Aa Bb": 1.00} # generation 0, Tom is heterozygous
]

n_per_generation = [
    1
]

trait_b_tr = {"BB": "AA", "Bb": "Aa", "bb": "aa"}
trait_b_rev_tr = {"AA": "BB", "Aa": "Bb", "aa": "bb"}

for gen in range(0, kGenerations):
# for gen in range(0, 6):
    # double the amount of people in the next generation
    n_next_gen = n_per_generation[-1] * 2
    n_per_generation.append(n_next_gen)

    # determine genotypes for the next generation
    cur_gen_genotypes = genotype_per_generation[-1]
    # print(cur_gen_genotypes)
    new_gen_genotypes = {genotype: 0.00 for genotype in all_genotypes}

    # go through each genotype in the current generation
    for cur_gen_genotype in cur_gen_genotypes.keys():
        cur_gen_prevalence = cur_gen_genotypes[cur_gen_genotype]
        # print(cur_gen_prevalence)
        traits = cur_gen_genotype.split(" ")
        trait_a_genotype = traits[0]
        trait_b_genotype = traits[1]
        trait_b_genotype_tr = trait_b_tr[trait_b_genotype]

        mate_trait_a_genotype = "Aa"
        mate_trait_b_genotype = "Bb"
        mate_trait_b_genotype_tr = "Aa"

        for possible_child_trait_a_genotype in ["AA", "Aa", "aa"]:
            trait_a_base_ratio = OGT[trait_a_genotype]\
                                    [mate_trait_a_genotype]\
                                    [possible_child_trait_a_genotype]


            for possible_child_trait_b_genotype in ["BB", "Bb", "bb"]:
                possible_child_trait_b_genotype_tr = \
                    trait_b_tr[possible_child_trait_b_genotype]
                trait_b_base_ratio = OGT[trait_b_genotype_tr]\
                                        [mate_trait_b_genotype_tr]\
                                        [possible_child_trait_b_genotype_tr]

                child_overall_genotype = possible_child_trait_a_genotype + " " \
                                         + possible_child_trait_b_genotype
                possibility_from_pairing = cur_gen_prevalence \
                                           * trait_a_base_ratio \
                                           * trait_b_base_ratio

                new_gen_genotypes[child_overall_genotype] += \
                    possibility_from_pairing

    genotype_per_generation.append(new_gen_genotypes)    

# determine final numbers in the final generation
kth_gen_genotype_ratios = genotype_per_generation[-1]
kth_gen_individuals = n_per_generation[-1]
final_prob = 0.0

# get probability of heterozygosity and non-heterozygosity
p_heterozygous = kth_gen_genotype_ratios["Aa Bb"]
p_non_heterozygous = 1.00 - p_heterozygous

# get the probability for each number of heterozygous individuals from
# min threshold to total num of individuals
for n_heterozygous in range(nThreshold, kth_gen_individuals + 1):

    n_non_heterozygous = kth_gen_individuals - n_heterozygous
    combinations = combination_without_replacement(int(kth_gen_individuals),
                                                   int(n_heterozygous))
    prob = float(combinations) \
           * math.pow(p_heterozygous, n_heterozygous) \
           * math.pow(p_non_heterozygous, n_non_heterozygous)
    final_prob += prob

print(round(final_prob, 5))
