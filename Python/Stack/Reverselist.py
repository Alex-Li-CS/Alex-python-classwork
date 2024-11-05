my_string = input("Enter a string")
list1 = []
list1copy = []
list2 = []
for char in my_string:
    list1.append(char)
    list1copy.append(char)
while len(list1) != 0:
    list2.append(list1.pop())
if list1copy == list2:
    print(my_string, "is a palindrome")
else:
    print(my_string, "is not a palindrome")