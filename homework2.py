def computey(hours, rate):
    if(hours > 40):
        pay = (40*rate*1.0) + ((hours - 40)*1.5*rate)
    else:
        pay = hours*rate    
    return pay

try:
    hours = float(input("Enter Hours : "))
    rate = float(input("Enter Rate : "))
    if hours < 0 or rate < 0:
        raise Exception
    else:
        print("Pay : " , computey(hours, rate))
except Exception:
    print("Error, please enter numeric input between 0 and 100 ")   