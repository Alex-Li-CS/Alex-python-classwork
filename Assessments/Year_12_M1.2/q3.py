# Write a python function sum_rows(matrix) that takes a 2d array(list of lists) and returns a list containing the sum of elements in each row
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def sum_rows(matrix):
    a = 0
    b = 0
    c = 0
    for i in range(0, 3):
        a += matrix[0][i]
    for k in range(0, 3):
        b += matrix[1][k]
    for j in range(0,3):
        c += matrix[2][j]
    new_matrix = [a, b, c]
    return(new_matrix)
print(sum_rows(matrix))