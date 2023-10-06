seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
seq1 = seq.replace("A","t").replace("C","g")
seq2 = seq1.replace("T","a").replace("G","c")
seq3 = seq2.upper()
print(seq3)