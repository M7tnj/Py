def convert(user_input):
    return user_input.replace(":)","🙂").replace(":(", "🙁")
    

def main():
    user_input = input("Please enter your text: ")
    user_input = convert(user_input)
    print(user_input)


main()