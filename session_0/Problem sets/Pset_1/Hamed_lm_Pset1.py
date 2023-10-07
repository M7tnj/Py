seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
a = seq.count("A")
t = seq.count("T")
c = seq.count("C")
g = seq.count("G")
at_content = (a+t)/(a+t+c+g)*100
at_content = round(at_content)
print (at_content)
