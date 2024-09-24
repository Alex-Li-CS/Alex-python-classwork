table = int(input())
startnum = int(input())
endnum = int(input())
pupilName = str(input())
def multiples(table, startnum, endnum, pupilName):
    print("Hi, " + str(pupilName) + " ... here is your times table")
    for x in range(startnum, endnum + 1):
        print(str(table) + " * " + str(x) + " = " + str(table * x))
multiples(table, startnum, endnum, pupilName)
