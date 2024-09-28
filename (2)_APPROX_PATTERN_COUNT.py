def ApproximatePatternCount(Text, Pattern, d):
        count = 0
        for i in range(len(Text)-len(Pattern)+1):
            SUBSTR = Text[i:i+len(Pattern)]
            mismatch_count = sum(1 for p, t in zip(Pattern, SUBSTR) if p != t)

            if mismatch_count <= d:
                count = count + 1
        return count
ANS = ApproximatePatternCount("CATGCCATTCGCATTGTCCCAGTGA", "CCC", 2)
print(ANS)