width = float(input("Enter your width"))
length = float(input("Enter your length:"))
nopaint = float(input("Enter the area in which paint cannot be coated"))
Area = width * length
Real_Area = Area - nopaint
Paint_req = Real_Area // 11 + 1
print(Paint_req)
