def add_names():
    names = [""] * 10
    while len(names) < 10:
        try:
            choice = int(input("Input 1 to add name, 2 to display the list of names, 3 to quit entering names "))
        except ValueError:
            print("Please enter a valid number (1, 2, or 3).")
            continue
        if choice == 1:
            name = input("Enter a name: ")
            place = int(input("Enter position (1 to 10): "))
            if 1 <= place <= 10:
                names[place - 1] = name
            else:
                print("Invalid position.")
            break
        elif choice == 2:
            print(names)
        elif choice == 3:
            print("Program Terminating")
            break

add_names()

