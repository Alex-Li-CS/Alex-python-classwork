def proc1(x:int, y:int)->None:
    x = x - 2
    y[0] = 0
#end procedure

m = 8
n = [10] #n is now a reference
proc1(m, n)
print(m, n)

