def recurTotal(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recurTotal(arr[1:])