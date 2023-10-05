seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

complement_seq = seq.replace("T","x").replace("G","z").replace("A","T").replace("C","G").replace("x","A").replace("z","C")

print(complement_seq)