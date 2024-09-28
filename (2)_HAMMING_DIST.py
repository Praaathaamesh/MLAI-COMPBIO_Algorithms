#here we have two sequences S1 and S2

S1 = "TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC"
S2 = "GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA"

# here we have an empty variable NUM
NUM = 0

# use for loop for comparing indices of S1 with S2  
for i in range(len(S1)):
    if S1[i]!=S2[i]:
        NUM += 1  # if mismacth is seen, we will add 1 to the empty varibale above.

# then we will print the "not so empty" NUM variable.
print(NUM)