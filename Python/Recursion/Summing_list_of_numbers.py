numbers= [3,4,2,8,1]
def iterTotal(arr)->int:
    z = 0
    for i in range(len(arr)):
        z += arr[i]
    return z
print(iterTotal(numbers))