def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    user_input = input("Enter an Emoticons : ")
    result = convert(user_input)
    print(result)
if __name__ == "__main__":
    main()
  
