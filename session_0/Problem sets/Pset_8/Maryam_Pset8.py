def dollars_to_float(dollars):
    x = float(dollars.replace('$', ''))
    return x

def percent_to_float(percent):
    percentage = float(percent.replace('%', '')) / 100
    return percentage

dollars = "$50.00"
percent = "15%"
print(dollars_to_float(dollars)) 
print(percent_to_float(percent)) 