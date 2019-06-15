def dna_reverse_complement(sequence):
    rev_com = ""
    complements = {"A": "T", "C": "G", "G": "C", "T": "A"}

    for nuc in sequence[::-1]:
        rev_com += complements[nuc]

    return rev_com
