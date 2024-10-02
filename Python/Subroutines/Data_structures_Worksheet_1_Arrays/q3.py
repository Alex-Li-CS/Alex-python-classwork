name = ["John, Bob"]
namePlace = input("Enter Name")
for i in range(len(name)-1):
    if namePlace == name[i]:
        print("record number for", namePlace, "is", i + 1)#
    else:
        print("name not found")