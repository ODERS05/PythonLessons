text1 = ""
while True:
    text = input("Please enter string: ")
    if text == "done":
        print("Bye !")
        break
    for letter in text:
        if letter == "!" or letter == ":" or letter == "." or letter == "," or letter == "?":
            continue
        else:
            text1 = text1 + letter.replace(" \n", " ").upper()
    print(text1)
    text1 = ""
    