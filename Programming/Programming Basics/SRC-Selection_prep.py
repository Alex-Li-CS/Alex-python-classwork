print("Select one of the following options: ") 
print("Enter A for Multiply: ") 
print("Enter B for Divide: ") 
print("Enter C for Add: ") 
print("Enter D for subtract: ") 
print("Enter E for Remainder Division: ")  

one = int(input("Enter a number")) 
two = int(input("Enter a second number")) 
option = str(input("Enter the letter for which operation you want to perform")) 
if option.lower() !=  "a" or option.lower() != "b" or  option.lower() != "c" or option.lower() != "d" or option.lower() != "e": 
    option = str(input("Enter the letter for which operation you want to perform")) 

if option.lower() == "a":
    print(one * two )
if option.lower() == "b":
    print(one // two )    
if option.lower() == "c":
    print(one + two )    
if option.lower() == "d":
    print(one - two )    
if option.lower() == "e":
    print(one % two )