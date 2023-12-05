def converter(input_string):
 input_string = input_string.replace(":(", "🙁")
 input_string = input_string.replace(":)", "🙂")
 return input_string

def main():
   user_input = input("Enter an Emoticons:")
   result = convert(user_input)
   print(result)
main()
