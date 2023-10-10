while True:
    try:
        text = input("Please enter two words: ")
        if text == "":
            print("-- bye !!")
            break
        words = text.split()
        word1 = words[0]
        word2 = words[1]
        if word1.isdigit() and word2.isdigit():
            raise Exception
        if word1 < word2: 
            print(f"{word1} come first")
        else:
            print(f"{word2} come first")
    except Exception:
        print

