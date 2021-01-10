def to_rna(dna_strand):
    dna_rna_map = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    return "".join(dna_rna_map.get(i, "") for i in dna_strand)
