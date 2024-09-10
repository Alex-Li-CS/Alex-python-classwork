x =  float(input("Please enter a three digit number"))
while x > 1000:
    x =  float(input("Please enter a three digit number"))
y = x // 100 * 100
c = x - y
d = c // 10 * 10
f = x - d - y
print(y, d, f)