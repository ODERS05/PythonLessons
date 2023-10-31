with open('romeo.txt', 'r') as file:
    list = []
    for line in file:
        text = line.split()
        for word in text:
            if word not in list:
                list.append(word)
    list.sort()
    print(list)


