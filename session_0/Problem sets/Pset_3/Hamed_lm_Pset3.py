dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

cut = dna.find("GAATTC")
first_frag = dna[:cut]
second_frag = dna[cut:]
print(dna)
print(first_frag)
print(second_frag)
size_of_1st_frag = print(len(first_frag))
size_of_2nd_frag = print(len(second_frag))
