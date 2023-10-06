# always check the output
# your output will be ['T', 'G', 'A', 'C', 'T', 'A', 'G', 'C', 'T', 'A', 'A', 'T', 'G', 'C', 'A', 'T', 'A', 'T', 'C', 'A', 'T', 'A', 'A', 'A', 'C', 'G', 'A', 'T', 'A', 'G', 'T', 'A', 'T', 'G', 'T', 'A', 'T', 'A', 'T', 'A', 'T', 'A', 'G', 'C', 'T', 'A', 'C', 'G', 'C', 'A', 'A', 'G', 'T', 'A']


dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

complement = [x.replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper() for x in dna] # list methods haven't been tought yet

print(complement)
