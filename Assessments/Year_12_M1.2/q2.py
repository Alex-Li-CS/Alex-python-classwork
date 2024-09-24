# Write a python function classify_grade(percentage) that takes a percentage as input and returns the grade according to the following classifications:
# A = +90, B = +80, C = +70, D = +60, F = -60
n = int(input("Enter here:"))
def sum_of_even_numbers(n):
    sum = 0
    for i in range(2, n+1, 2):
        sum += i
    return(sum)
print(sum_of_even_numbers(n))
percentage = int(input("Input grade here:"))
def classify_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
print(classify_grade(percentage))