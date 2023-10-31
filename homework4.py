numbers = []
count = 0
sum = 0
print("typing 'done' will exit the program")
while True:
    try:
        number = input("Please enter an integer: ")
        if number == 'done':
            print("---------- Bye !! --------------")
            break
        numbers.append(number)
        count = count + 1
        sum += int(number)
        print(numbers, "average =", sum/count)
    except ValueError:
        continue
