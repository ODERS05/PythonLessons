seconds = input("Enter seconds : ")
seconds = int(seconds)
hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
seconds1 = seconds - (hours * 3600) - (minutes * 60)
print(seconds, " seconds is ", hours, " hours, ", minutes, " minutes, ", seconds1, " seconds")