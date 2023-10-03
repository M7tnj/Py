sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
complement_of_dna = sequence.replace("A","X").replace("G","Y").replace("T","A").replace("C","G").replace("X","T").replace("Y","C")
print(complement_of_dna)