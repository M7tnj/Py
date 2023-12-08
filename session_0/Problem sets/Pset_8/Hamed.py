# tip_calculator
def tip_calculator():
    tot = dollar_to_float(input("tot bill:"))
    tip_percent = tip_to_float(input("percent:"))
    tip = tot * tip_percent /100
    print(tip)

def dollar_to_float(x):
    dollars = float(x.replace("$",""))
    return dollars

def tip_to_float(t):
    pay = float(t.replace("%",""))
    return pay

tip_calculator()
