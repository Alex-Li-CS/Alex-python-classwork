def remove(lst):
    size = len(lst)

    if size != 0:
        character = int(input("What is the position of the character you wish to remove"))
        for x in range(character, len(lst) - 1):
            lst[x] = lst[x + 1]
            lst.remove(lst[len(lst)-1])
    else:
       print("Queue is empty")
my_list = [10, 20, 30, 40, 50]
remove(my_list)
print(my_list)

