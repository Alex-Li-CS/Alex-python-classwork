#Write a program that has three prompts for the user to enter the current time. THe first will be the hours (12hr clock)
#the second will be the minutes and the third will be either Am or pm. the program should then output the number of mintues since midnight
hours = int(input("Please enter the hour:"))
minutes = int(input("Please enter minutes here:"))
period = input("Please enter am or pm")
while period != "am" and period != "pm":
    period = input("Please enter am or pm")
if period == "am":
    b = hours * 60
    z = b + minutes
    print(z)
else:
    hour = hours + 12
    b = hour * 60
    z = b + minutes
    print(z)