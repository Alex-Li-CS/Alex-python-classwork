# Given a one dimension array of integers. Write a procedure to output the highest value in the array
my_array = [8, 1, -6, 9, 15, 7, 2]
max = 0
for x in my_array:
    if max < x:
        max = x
print(max)

# Which line of code would need to be altered to change it into a function
## my_array needs to be a function

#Write the line of code that would need to replace it
def my_array()
    
# Write the line of code to call the function and output the result using the list my_array
def my_array(a):
    max = 0
    for x in a:
        if max < x:
            max = x
    return max
