# Write code the repeatedly prompts the user to enter a non negative integer.
# If the user enter a negative integer the program stops prompting for new numbers and outputs the average 
# of those entered 
a = []
x = int(input())
while x > 0:
    a.append(x)
    x = int(input())
if a:
    total = sum(a)
    average = total // len(a)
    print(average)
