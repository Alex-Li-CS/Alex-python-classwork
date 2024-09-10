# Write code that prompts the user to enter ten (non negative) integers,
# After entering the ten integers the program should output the total with a meaningful message
num_list = []
for i in range(0, 10):
    num = int(input(""))
    num_list.append(num)
total = sum(num_list)
print("the total of the 10 numbers is:", total)
