def dollars_to_float(cost):
    return float(cost.replace("$" , ""))

def percent_to_float(percentage):
    return float(percentage.replace("%" , "")) / 100

tip = input("tip> ")
print(dollars_to_float(tip))
print(percent_to_float(tip))
