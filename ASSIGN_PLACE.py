Genome = open('Vibrio_cholerae.txt','r').read()

Pattern = "CTTGATCAT"

 

Position = []

for i in range(len(Genome) - len(Pattern)+1):

    if Genome[i:i + len(Pattern)] == Pattern:

        Position.append(i)

print(*Position)