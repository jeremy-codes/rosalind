DNA_CODON_TABLE = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
}

DNA_CODON_TABLE_U_SUB_T = {
    k.replace("U", "T") : DNA_CODON_TABLE[k] for k in DNA_CODON_TABLE
}

TRANSITION_TRANVERSION = {
    "AxG": "transition",
    "CxT": "transition",
    "GxA": "transition",
    "TxC": "transition",

    "AxC": "transversion",
    "AxT": "transversion",
    "CxA": "transversion",
    "CxG": "transversion",
    "GxC": "transversion",
    "GxT": "transversion",
    "TxA": "transversion",
    "TxG": "transversion"
}

MONOISOTOPIC_MASS_TABLE = {
    "A": 71.03711,
    "C": 103.00919,
    "D": 115.02694,
    "E": 129.04259,
    "F": 147.06841,
    "G": 57.02146,
    "H": 137.05891,
    "I": 113.08406,
    "K": 128.09496,
    "L": 113.08406,
    "M": 131.04049,
    "N": 114.04293,
    "P": 97.05276,
    "Q": 128.05858,
    "R": 156.10111,
    "S": 87.03203,
    "T": 101.04768,
    "V": 99.06841,
    "W": 186.07931,
    "Y": 163.06333
}

OFFSPRING_GENOTYPE_TABLE = {
    # Parent 1
    "AA": {
        # Parent 2
        "AA": {
            # Child Genotype and Rate
            "AA": 1.00,
            "Aa": 0.00,
            "aa": 0.00
        },
        "Aa": {
            # Child Genotype and Rate
            "AA": 0.50,
            "Aa": 0.50,
            "aa": 0.00
        },
        "aa": {
            # Child Genotype and Rate
            "AA": 0.00,
            "Aa": 1.00,
            "aa": 0.00
        }
    },
    # Parent 1
    "Aa": {
        # Parent 2
        "AA": {
            # Child Genotype and Rate
            "AA": 0.50,
            "Aa": 0.50,
            "aa": 0.00
        },
        "Aa": {
            # Child Genotype and Rate
            "AA": 0.25,
            "Aa": 0.50,
            "aa": 0.25
        },
        "aa": {
            # Child Genotype and Rate
            "AA": 0.00,
            "Aa": 0.50,
            "aa": 0.50
        }

    },
    # Parent 1
    "aa": {
        # Parent 2
        "AA": {
            # Child Genotype and Rate
            "AA": 0.00,
            "Aa": 1.00,
            "aa": 0.00
        },
        "Aa": {
            # Child Genotype and Rate
            "AA": 0.00,
            "Aa": 0.50,
            "aa": 0.50
        },
        "aa": {
            # Child Genotype and Rate
            "AA": 0.00,
            "Aa": 0.00,
            "aa": 1.00
        }
    }
}

PHRED_PLUS33_LIST = [
    "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">",
    "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"
]

PHRED_PLUS33_DICT = {
    PHRED_PLUS33_LIST[i]: i for i in range(0, len(PHRED_PLUS33_LIST))
}
