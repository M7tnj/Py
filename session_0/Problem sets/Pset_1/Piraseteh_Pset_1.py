dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

a_count = dna_seq.count("A")
t_count = dna_seq.count("T")
at_count = dna_seq.count("AT")
ta_count = dna_seq.count("TA")
total_at_count = a_count + t_count

print("There are", a_count, "Adenins in this sequence")

print("There are", t_count, "Thymines in this sequence")

print("There are", at_count, "\"AT\" basepairs in this sequence")

print("There are", ta_count, "\"TA\" basepairs in this sequence")

print("There is a total of", total_at_count, "Adenins and Thymines in this sequence")