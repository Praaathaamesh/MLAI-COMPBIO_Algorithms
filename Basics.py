# Let us write the simplest program with shittiest implicatory capabilities.
PROT="ADGLDVWT"

# Splice the statement line using []. Here, positioning (indexing) of a string starts with 0.
First_Residue=PROT[0]
# Here, Start index is INCLUSIVE and End Index is EXCLUSIVE.
First_FIVE_Residues=PROT[0:5] 

# Now print the custom variable.
print(First_Residue)
print(First_FIVE_Residues)

# Let us CONCATANATE using '+' & print it.
CONCAT=First_Residue+First_FIVE_Residues
print(CONCAT)

# Let us REPLACE G with M. (Since, ".replace()"  is a "method" it requires variable to function with and utilised by putting period after the variable.)
# Method looks somewhat like this- '''variable.method()''' (THE THINGY IN THE BRACKET IS CALLED "argument")
REPLACE=PROT.replace('G','M')
print(REPLACE)

# Now let us COUNT specific residue using function "count()".
count_D_residues=PROT.count('D')
count_W_residues=PROT.count('W')
# Print the results using ".str()" method to convert the FPN into string datatype.
print('No. of D residues', str(count_D_residues))
print('No. of W residues', str(count_W_residues))

# Let us FIND a residue using ".find()" method.
FIND=PROT.find("A")
print(str(FIND))