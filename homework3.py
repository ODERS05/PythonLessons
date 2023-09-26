number_of_input = 0
sum_of_input = 0
while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    else:
        try:
            number = int(number)
            sum_of_input = sum_of_input + number
            number_of_input = number_of_input + 1
        except Exception:
            print("Invalid input. Please enter a number")    
if number_of_input > 0:
    average = float(sum_of_input) / number_of_input
    print("Sum of input numbers: ",sum_of_input)
    print("Number of input: ", number_of_input) 
    print("Average of input numbers: ", average)
else:
    print("No numbers enterned")