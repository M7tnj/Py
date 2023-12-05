dollar = input("Please enter how much you paid using the following format: $##.##\n $")
percent = input("Please enter Tip percentage: %")

def dollar_to_float(dollar):
    if dollar.startswith("$"): 
       dollar = dollar.replace("$", "") 
    dollar = float(dollar) 
    return dollar 
    
def percent_to_float(percent):
    if percent.endswith("%"): 
        percent = percent.replace("%", "") 
    percent = float(percent) 
    return percent 

print(f"you have paid a total of {dollar_to_float(dollar)} dollars for your food and tipped {percent} percent")