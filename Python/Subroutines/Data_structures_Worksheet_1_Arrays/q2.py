name = []

def find(student):
    for i in range(len(name)):
        if name[i] == student:
            print(student + " found at record number " + str(i + 1))
            return
    print(student + " not found.")
def input_names():
    num = int(input("How many names do you want to enter? "))
    for _ in range(num):
        name.append(input("Enter a name: "))
input_names() 
student = input("Enter the name to search for: ")
find(student)
