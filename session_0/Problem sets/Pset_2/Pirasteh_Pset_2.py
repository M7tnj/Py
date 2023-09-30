dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

complement = [x.replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper() for x in dna]

print(complement)
