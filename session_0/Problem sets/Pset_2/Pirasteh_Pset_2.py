# always check the output
# your output will be ['T', 'G', 'A', 'C', 'T', 'A', 'G', 'C', 'T', 'A', 'A', 'T', 'G', 'C', 'A', 'T', 'A', 'T', 'C', 'A', 'T', 'A', 'A', 'A', 'C', 'G', 'A', 'T', 'A', 'G', 'T', 'A', 'T', 'G', 'T', 'A', 'T', 'A', 'T', 'A', 'T', 'A', 'G', 'C', 'T', 'A', 'C', 'G', 'C', 'A', 'A', 'G', 'T', 'A']


dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

complement = dna.replace("A","t").replace("T","a").replace("G","c").replace("C","g")

#ATTENTION: it turns out, the replace function is pretty case sensetive
complement = complement.upper()

print(complement)
