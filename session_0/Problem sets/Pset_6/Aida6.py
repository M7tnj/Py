# Einestin
def calculate_energy(m,c):
    c = 300000000
    energy = (m*(c**2))
    return energy

mass = int(input("Enter the mass in kilo: "))
print(calculate_energy(m,c))




# AT_Calculator
def AT_content(seq):
    AT_count = dna_seq.count("A") + dna_seq.count("T")
    total = len(dna_seq)
    AT_content = (AT_count / total) * 100
    return AT_content

dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
result = AT_content(dna_seq)
print(result)




# complementary_Dna







# fragment_calculator
def feragment_size(dna_seq):
    cut_size = dna_seq.find("GAATTC")
    f1_size = cut_size + 1 
    f2_size = len(dna_seq) - f1_size
    return f1_size , f2_size

dna_seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
fragment1 , fragment2 = feragment_size(dna_seq)
print (fragment1 , fragment2)




# indoor
def convert_to_lpwercase():
    user_input = input("Enter your input: ")
    lowercase_input = user_input.lower()
    print(lowercase_input)

convert_to_lpwercase()




# playback
def replace_space_with_periods():
    user_input = input("Enter a str: ")
    modified_input = user_input.replace("","...")
    print(modified_input)