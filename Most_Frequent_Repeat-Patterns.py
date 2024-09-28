text = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
k = 3
def FrequencyMap(text, k):   

    freq = {}   

    n = len(text)   

    for i in range(n-k+1):   

        pattern = text[i:i+k]   

        if pattern in freq:   

            freq[pattern] += 1   

        else:   

            freq[pattern] = 1   

    return freq   

def FrequentKmers(text, k):   

    kmers = []   

    freq = FrequencyMap(text, k)   

    m = max(freq.values())   

    for most_frequent_kmer in freq:   

        if freq[most_frequent_kmer] == m:   

          kmers.append(most_frequent_kmer)   

    return kmers   

print("most frequent 4-mer is")  

print(FrequentKmers(text, k)) 