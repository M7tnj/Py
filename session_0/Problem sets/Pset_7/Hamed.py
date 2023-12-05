def converter(txt):
    txt = txt.replace(":)", "🙂")
    txt = txt.replace(":(", "🙁")
    return txt


face = converter(input(">"))
print(face)
# what should i do about main ??? :/
