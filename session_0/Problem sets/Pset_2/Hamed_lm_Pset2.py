# add pseudocode
# always look up for the best pythonic style (one line between input - proceccing and the output)

# defining the given sequence
sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

# replace each basepair to its complement
complement_of_dna = sequence.replace("A","X").replace("G","Y").replace("T","A").replace("C","G").replace("X","T").replace("Y","C")

# print the output
print(complement_of_dna)
