def genome(seg):
    yu = []
    cnt = 0
    dit = dict(A = 0, C = -1, G = 1, T = 0)
    for i in seg:
        cnt += dit[i]
        yu.append(cnt)
    return yu


ANS = genome("GAGCCACCGCGATA")
print(ANS)