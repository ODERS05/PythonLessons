def calculate_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

while True:
    try:
        grade = int(input("Enter your Score: "))
        if grade < 0 or grade > 100:
            raise Exception
        else:
            result = calculate_grade(grade)
            print("Grade is ", result)
    except Exception:
        print("Error, please enter numeric input between 0 and 100")
        