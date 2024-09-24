Year = str(input("Please enter your "))
LeapYear = False
if (mod(Year, 4) == 0):
    LeapYear = True
if (mod(Year, 100) == 0):
    LeapYear = False
if (mod(Year, 400) == 0):
    LeapYear = true