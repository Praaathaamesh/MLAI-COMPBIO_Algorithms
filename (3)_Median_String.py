def hamming_distance(pattern, text):
    """
    Compute the Hamming distance between two strings of equal length.
    """
    distance = 0
    for i in range(len(pattern)):
        if pattern[i] != text[i]:
            distance += 1
    return distance


def d(pattern, dna):
    """
    Compute the total Hamming distance between a pattern and a collection of DNA strings.
    """
    distance = 0
    k = len(pattern)
    for text in dna:
        min_hamming = float('inf')
        for i in range(len(text) - k + 1):
            kmer = text[i:i+k]
            hamming = hamming_distance(pattern, kmer)
            if hamming < min_hamming:
                min_hamming = hamming
        distance += min_hamming
    return distance


def median_string(k, dna):
    """
    Find a k-mer pattern that minimizes the total Hamming distance among all possible choices of k-mers.
    """
    best_pattern = None
    best_distance = float('inf')
    for i in range(4**k):  # Iterate over all possible k-mers
        pattern = ''.join(['ACGT'[(i >> (2*j)) & 3] for j in range(k)])
        distance = d(pattern, dna)
        if distance < best_distance:
            best_distance = distance
            best_pattern = pattern
    return best_pattern


# Example usage
k = 7
dna = ['CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC', 'GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC', 'GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG']
result = median_string(k, dna)
print(result)
