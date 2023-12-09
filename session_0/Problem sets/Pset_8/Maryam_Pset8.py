def main():
    X = dollars_to_float(input("Enter your total price:"))
    Tip= percent_to_float(input("Enter your percent:"))
    tip = X * Tip 
    print(f"leave ${tip:.2f}")

def dollars_to_float(dollars):
    x = float(dollars.replace("$", ""))
    return x

def percent_to_float(percent):
    percentage = float(percent.replace("%", "")) / 100
    return percentage
    
main()
