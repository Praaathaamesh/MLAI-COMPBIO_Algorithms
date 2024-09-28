def TheoSpec(peptide):
    AminoAcidMass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


    ls = []

    l = len(peptide)
    looped = peptide + peptide
    for start in range(0, l):
        for length in range(1, l):
            ls.append((looped[start:start + length]))
    ls.append(peptide)

    def calculate_mass(element):
        return sum(AminoAcidMass[aa] for aa in element)

    sorted_elements = sorted(ls, key=calculate_mass)

    for element in sorted_elements:
        mass = calculate_mass(element)
        
        print(mass, end=" ")

peptide = "FCDPYLGLYSCMTHLRWWFAPPWGKYKVIDPDEIWCDA"

TheoSpec(peptide)
