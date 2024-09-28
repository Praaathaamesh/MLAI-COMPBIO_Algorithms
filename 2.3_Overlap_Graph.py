seq = ""
reads = seq.split()

#<INSTRUCTION> Splice out the required substring
for i in reads:
    comp1 = [read[1:] for read in reads]
    comp2 = [read[:-1] for read in reads]

sym = [':'] # Set for adding ":" to the output

#<INSTRUCTION> Comparison and Output
similar_groups = {}
for j, read1 in enumerate(comp1):
    for k, read2 in enumerate(comp2):
        if read1 == read2 and j != k:
            if j not in similar_groups:
                similar_groups[j] = []
            similar_groups[j].append(reads[k])

# Output similar strings
for idx, similar_reads in similar_groups.items():
    print(reads[idx]+sym[0], ' '.join(similar_reads))