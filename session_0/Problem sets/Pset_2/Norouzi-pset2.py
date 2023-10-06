seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
i1 = seq.replace("A","t")
i2 = i1.replace("T","a")
i3 = i2.replace("C","g")
i4 = i3.replace("G","c")
new_seq = i4.upper()
print(new_seq)
