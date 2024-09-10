# Write a program that prompts the user for an integer representing the number of minutes that have passed since midnight.
# The program should then print the time as displayed on the digital clock ie: two numbers: the number of hours
# (between 00 adn 23) and the number of minutes (between 00 and 59) seperated by a colon.
pastmid = int(input("Input number of minutes since midnight:"))
hour = pastmid // 60
minute = pastmid % 60
minute = f"{minute:02}"
if hour > 24:
    hour = hour - 24
if hour < 10:
    hour = f"{hour:02}"
print(f"{hour}:{minute}")