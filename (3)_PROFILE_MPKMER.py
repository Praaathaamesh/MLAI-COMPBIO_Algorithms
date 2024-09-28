def profile_most_probable_kmer(text, k, profile):
    n = len(text)
    max_prob = -1
    most_probable_kmer = ""

    for i in range(n - k + 1):
        kmer = text[i:i+k]
        prob = 1

        for j in range(k):
            if kmer[j] == 'A':
                prob *= profile[0][j]
            elif kmer[j] == 'C':
                prob *= profile[1][j]
            elif kmer[j] == 'G':
                prob *= profile[2][j]
            elif kmer[j] == 'T':
                prob *= profile[3][j]

        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer

    return most_probable_kmer

# Test the function with the given sample input
text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
k = 5
profile = [
    [0.2, 0.2, 0.3, 0.2, 0.3],
    [0.4, 0.3, 0.1, 0.5, 0.1],
    [0.3, 0.3, 0.5, 0.2, 0.4],
    [0.1, 0.2, 0.1, 0.1, 0.2]
]

result = profile_most_probable_kmer(text, k, profile)
print(result)
