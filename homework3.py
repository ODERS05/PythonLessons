def num_divide3(number):
    count = 0
    for i in range(1, number + 1):
        if i %3 == 0:
            count = count + 1
    return count

while True:
    try:
        number = input("Enter a positive integer: ")
        if number == "done":
            print("Bye!")
            break
        else:
            number = int(number)
        if number < 0:
            raise Exception
        else:
            result = num_divide3(number)
            print(f"Numbers divisible by 3 among numbers from 1 to {number} : {result}")
    except Exception:
        print("Please enter a positive number") 

