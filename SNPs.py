# Following program will provie the user the positioning of SNPs (Single Nucleotide Polymorphism) positions within two distinctive DNA sequences by ci=omparitive FASTA analysis.
sequencelist= []
def snpdetect(sq1, sq2):                                     # Define function name and the variables of the sequences
    for i in (range(len(sq1))):                              # Iterate first variable using for in loop (here, "range" = To analyse the legth and "len" = To return the number of items.)
        if sq1[i] != sq2[i]:                                 # Use comparator function "!=" (Means "not equal to") and append to pluck values in empty list (Use if conditional statement which uses true or false value of a variable.)
            sequencelist.append(i)
    return sequencelist

# Adding FASTAs
sq1 =input("Please paste FASTA 1:")
sq2 =input("PLease paste FASTA 2:")

print(snpdetect(sq1,sq2))                                    # Print the whole function again.