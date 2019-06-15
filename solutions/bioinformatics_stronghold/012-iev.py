"""Solution for Bioinformatics Stronghold Problem ID: IEV

Problem Title: Calculating Expected Offspring
Link: http://rosalind.info/problems/iev
"""

from rosalindutils.constants import OFFSPRING_GENOTYPE_TABLE as OGT

input_path = "data/rosalind_iev.txt"
input_list = open(input_path, "r").read().rstrip().split(" ")

couple_genotypes = ["AA-AA", "AA-Aa", "AA-aa", "Aa-Aa", "Aa-aa", "aa-aa"]
couple_counts = {couple_genotypes[i]: int(input_list[i]) for i in range(0, 6)}

total_dom_offspring = 0.0

for couple_gt in couple_genotypes:
    father_gt, mother_gt = couple_gt.split("-")
    child_gt_ratios = OGT[father_gt][mother_gt]
    child_dom_pt_ratio = child_gt_ratios["AA"] + child_gt_ratios["Aa"]

    n_dom_offspring = 2.0 * float(couple_counts[couple_gt]) * child_dom_pt_ratio
    total_dom_offspring += n_dom_offspring

print(total_dom_offspring)
