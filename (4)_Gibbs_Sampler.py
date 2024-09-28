import random

 

#### MAIN FUNCTION ####

def GibbsSampler(dna, k, t, numIterations):

    dna = dna.split(" ") # Prepare input dna string

    r = random.randint(0, (len(dna[0])-k+1)) # Generate random number

    motifs = [] # Generate starting motifs array, based on the random number

    for i in range(t):

        motifs.append(dna[i][r:r+k])

    bestMotifs = motifs[:]

    bestScore = ScoreMotifs(bestMotifs)

    for i in range(numIterations):

        strIndex = random.randint(0, t-1) # Random string to ignore/delete

        motifs.pop(strIndex)

        profile = updateProfile(motifs, k)

        newkmer = ProfileWeightedRandom(profile, k, dna[strIndex]) # Choose new kmer with the "weighted dice"

        motifs.insert(strIndex, ProfileWeightedRandom(profile, k, dna[strIndex])) # Insert in motifs array, in the same position

        if ScoreMotifs(motifs) < bestScore:

            bestMotifs = motifs[:]

            bestScore = ScoreMotifs(bestMotifs)

    return bestMotifs

 

#### OUTER LOOP - Call GibbsSampler N times, return best motifs array ####

def bestOfN(n, dna, k, t, numIterations):

    dic = {}

    for i in range(n):

        print("RUN ", i+1)

        ans = GibbsSampler(dna, k, t, numIterations)

        score = ScoreMotifs(ans)

        dic.update({tuple(ans):score})

    bestMotifs = min(dic, key=dic.get)

    return bestMotifs

 

#### AUXILIARY FUNCTIONS ####

def updateProfile(motifs, k):

    profile = [[1, 1, 1, 1] for x in range(k)] # Profile matrix initialized at 1 instead of 0

    for i in range(len(motifs)):

        for j in range(k):

            base = motifs[i][j]

            if base == 'A': profile[j][0] += 1

            if base == 'C': profile[j][1] += 1

            if base == 'G': profile[j][2] += 1

            if base == 'T': profile[j][3] += 1

    return  [[x / (len(motifs) + 4) for x in col] for col in profile] # Denominator -> number of motifs + 4

 

def ScoreMotifs (motifs):

    model = ''

    for i in range(len(motifs[0])): # Find most common base for every position -> create the model string

        dic = {}

        for j in range(len(motifs)):

            if motifs[j][i] in dic:

                dic[motifs[j][i]] += 1

            else:

                dic[motifs[j][i]] = 1

        model += max(dic, key=dic.get)

    score = 0

    for i in range(len(motifs)): # Compare each motif to the model, count differences

        for c in range(len(motifs[i])):

            if motifs[i][c] != model[c]: score += 1

    return score

 

def ProfileWeightedRandom(profile, l, str):

    kmerList = []

    for i in range(len(str)-l): # Find all kmer in str

        kmerList.append(str[i:i+l])

    probList = []

    for i in range(len(kmerList)): # Find probability of each kmer in str

        prob = 1

        for j in range(l):

            base = kmerList[i][j]

            if base == 'A': prob = prob * profile[j][0]

            if base == 'C': prob = prob * profile[j][1]

            if base == 'G': prob = prob * profile[j][2]

            if base == 'T': prob = prob * profile[j][3]

        probList.append(prob)

    kmer = random.choices(kmerList, weights=probList, k=1) # Choose a kmer (random weighted)

    return kmer[0]

 

#### EXAMPLE CALL ####

dna = "CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA"

ans = bestOfN(20, dna, 8, 5, 100)

print(*ans, sep=" ")