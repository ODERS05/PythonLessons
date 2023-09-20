try:
    score = int(input("Enter your score: "))
    if score > 100 or score < 0:
        pass 
    elif score >= 90:
        grade = 'A'
    elif score >= 80: 
        grade = 'B'  
    elif score >= 70:
        grade = 'C' 
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print("Grade is %s." % grade)
except Exception:
    print("Error, please enter numeric input between 0 and 100")    

