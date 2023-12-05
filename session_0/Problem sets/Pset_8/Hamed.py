# tip_calculator
def tip_calculator(tot_price):
    tip = (tot_price*15)/100
    return tip 
total = float(input("tot_price:"))
tip = tip_calculator(total)
print (tip)
