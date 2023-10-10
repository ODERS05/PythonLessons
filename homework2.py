text = input("Enter string: ")
backwards = text[::-1]
index = 0
while index < len(backwards):
    letter = backwards[index]
    print(letter)
    index += 1