seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
#String length
a = len(seq)
#Find the intersection
b = seq.find("GAATTC")+1
#FromTheBeginningOfTheStranToTheCuttingSite
seq1 = seq[0:22]
#ContinueFromTheCut
seq2 = seq[22:55]
#SizeBothSidesOfTheCut
solution = len(seq1),len(seq2)
#Print
print(solution)
