dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

cut1 = dna.find("AATTC")
cut2 = dna.find("AATTC")
first_frag = dna[:cut1]
second_frag = dna[cut2:]
print(dna)
print(first_frag)
print(second_frag)
size_of_1st_frag = print(len(first_frag))
size_of_2nd_frag = print(len(second_frag))
