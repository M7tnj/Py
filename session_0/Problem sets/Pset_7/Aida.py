def convert (str):
    # Replace :) to 🙂
    str = str.replace(":)" , "🙂")
    # Replace :( to 🙁
    str = str.replace (":(" , "🙁")
    return str

def main():
    input_str = input("string: ")
    converted_str = convert(input_str)
    print(converted_str)
    