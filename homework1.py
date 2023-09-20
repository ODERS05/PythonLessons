try:
    hours = int(input("Enter Hours : "))
    rate = float(input("Enter Rate : "))
    if(hours > 40):
        Calculate_salary = (40*rate*1.0) + ((hours - 40)*1.5*rate)
    else:
        Calculate_salary = hours*rate    
    print("Pay : " , Calculate_salary)
except:
    print("Error, please enter numeric input")    