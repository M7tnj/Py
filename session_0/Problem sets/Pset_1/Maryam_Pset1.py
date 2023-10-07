seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
a = seq.count("A")
b = seq.count("T")
c = (a+b)/len(seq)*100
d = round(c)
print(d)
