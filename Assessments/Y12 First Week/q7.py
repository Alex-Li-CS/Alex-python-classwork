# Given a two dimension array of integers, e.g.
# my 2d_array = {[0,1,2][3,5,10]{6,7,8}}
# Write a function to output the highest value in the array. You may use the function declared in the previous question

# After find the row and column of the maximum
a = [[0, 1, 2], [3, 5, 10], {6, 7, 8}]
x = a[0]
y = a[1]
z = a[2]
b = 0
c = 0
d = 0
e = 0
L = []
for h in x:
    if b < h:
        b = h
for j in y:
    if c < j:
        c = j
for o in z:
    if d < o:
        d = o

L.append(b)
L.append(c)
L.append(d)

for s in L:
    if e < s:
        e = s
print(e)
print(L.index(e))
print(a[L.index(e)].index(e))
