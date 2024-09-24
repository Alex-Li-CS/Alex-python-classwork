# Write a python function sum_of_even_numbers(n) that takes an integer n and returns tum of all even numbers from 1 to n. Your solution should use iteration 
# to accumulate the sum
def sum_of_even_numbers(n):
    z = 0
    for x in range(1, n+1):
        if x % 2 == 0:
            z += x
    return z
print(sum_of_even_numbers(6))