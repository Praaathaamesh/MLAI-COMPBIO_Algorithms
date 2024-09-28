def frequency_table(text, kmer_len):
    freq_map = {}
    nt = len(text)
    nk = kmer_len
    
    for i in range(0, nt-nk+1): # Range short by one
        pattern = text[i : i+nk]
        if not freq_map.get(pattern):
            freq_map[pattern] = 1
        else:
            freq_map[pattern] = freq_map[pattern] + 1
        
    return freq_map

def FindClumps(Text, k, L, t):
    Patterns = []
    n = len(Text)
    for i in range(n - L):
        Window = str(Text[i : i+L]) # End range needs to be in relation to "i"
        freqMap = frequency_table(Window, k)
        # You can interate dictionary keys. Previously, you converted the 
        # dictionary to a list (which removed your values) in order to iterate 
        # over it. Your conditional then became nonsensical.
        for s in freqMap:
            if freqMap[s] >= t:
                Patterns.append(s)
    
    return list(set(Patterns)) # limit output to unique values only


print(FindClumps("CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA", 5, 50, 4))