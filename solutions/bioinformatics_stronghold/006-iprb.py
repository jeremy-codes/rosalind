"""Solution for Bioinformatics Stronghold Problem ID: IPRB

Problem Title: Mendel's First Law
Link: http://rosalind.info/problems/iprb
"""

""" Theory:
DOM - homozygous dominant
HET - heterozygous
REC - homozygous recessive

Punnett Squares of all pairings and offspring dominance ratio:

1. DOMxDOM - 100%
    A    A
A   AA   AA
A   AA   AA

2. DOMxHET - 100%
    A    A
A   AA   AA
a   Aa   Aa

3. DOMxREC - 100%
    A    A
a   Aa   Aa
a   Aa   Aa

4. HETxHET - 75%
    A    a
A   AA   Aa
a   Aa   aa

5. HETxREC - 50%
    A    a
a   Aa   aa
a   Aa   aa

6. RECxREC - 0%
    a    a
a   aa   aa
a   aa   aa
"""


offspring_dominant_phenotype_probs = {
    "DOMxDOM": 1.00,
    "DOMxHET": 1.00,
    "DOMxREC": 1.00,
    "HETxHET": 0.75,
    "HETxREC": 0.50,
    "RECxREC": 0.00
}

pop_counts = {
    "DOM": 0,
    "HET": 0,
    "REC": 0,
    "TOT": 0
}

parent_genotypes = ["DOM", "HET", "REC"]

sum_of_probabilities = 0.0

input_file = "data/rosalind_iprb.txt"
with open(input_file, "r") as infile:
    line_split = infile.read().rstrip().split(" ")
    dom = float(line_split[0])
    het = float(line_split[1])
    rec = float(line_split[2])
    total = dom + het + rec

    pop_counts["DOM"] = dom
    pop_counts["HET"] = het
    pop_counts["REC"] = rec
    pop_counts["TOT"] = total

for parent_a_gt in parent_genotypes:
    for parent_b_gt in parent_genotypes:
        pop_counts_cp = {k: pop_counts[k] for k in pop_counts.keys()}

        # rate of selecting parent a
        parent_a_select_ratio = pop_counts_cp[parent_a_gt] \
                                / pop_counts_cp["TOT"]

        # reduce population by 1 now that parent a has been selected
        # ie cannot mate with self
        pop_counts_cp[parent_a_gt] -= 1
        pop_counts_cp["TOT"] -= 1

        # rate of selecting parent b
        parent_b_select_ratio = pop_counts_cp[parent_b_gt] \
                                / pop_counts_cp["TOT"]


        pair_prob = parent_a_select_ratio * parent_b_select_ratio
        dominance_key = parent_a_gt + "x" + parent_b_gt
        if dominance_key not in offspring_dominant_phenotype_probs.keys():
             dominance_key = parent_b_gt + "x" + parent_a_gt
        dominance_prob = pair_prob \
                         * offspring_dominant_phenotype_probs[dominance_key]

        sum_of_probabilities += dominance_prob

print(round(sum_of_probabilities, 5))
