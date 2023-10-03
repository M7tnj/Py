dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

cut_position = dna.find("GAATTC") + 1

first_fragment = dna[:cut_position]
second_fragment = dna[cut_position:]

print("Main DNA sequence =", dna)

print("The first fragment is" , first_fragment , "and has a lenght of" ,len(first_fragment), "nucleotides")

print("The second fragment is" , second_fragment , "and has a lenght of" ,len(second_fragment), "nucleotides")