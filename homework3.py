text = input("Please enter string: ")
index = 0
uppercase = 0
lowercase = 0
number = 0
character = 0

while index < len(text):
    letter = text[index]
    if letter.isupper():
        uppercase =  uppercase + 1
    elif letter.islower():
        lowercase = lowercase + 1
    elif letter.isdigit():
        number = number + 1
    else:
        character = character + 1
    index += 1
print(f"-  Uppercase letters: {uppercase}")
print(f"-  Lowercase letters: {lowercase}")
print(f"-  Numbers: {number}")
print(f"-  Other characters: {character}")