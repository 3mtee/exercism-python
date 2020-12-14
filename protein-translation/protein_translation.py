codon_protein = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCG": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": None,
    "UAG": None,
    "UGA": None
}


def proteins(strand: str):
    codons = get_codons(strand)

    result = []
    for codon in codons:
        protein = codon_protein[codon]
        if protein is None:
            break
        if protein not in result:
            result.append(protein)
    return result


def get_codons(strand):
    chunk_size = 3
    codons = [strand[i:i + chunk_size] for i in range(0, len(strand), chunk_size)]
    return codons
