A = str(input("Please input your original password:"))
attempt = int(input("Pick 1 to set password, Pick 2 to change it"))
def getPword(attempt):
    global A 
    if attempt == 1:
        A = str(input("Enter a password between 6-8 characters:"))
        while len(A) > 8 or len(A) < 6:  # Keep asking until the password is valid
            A = str(input("Password must be between 6-8 characters. Enter a new password:"))
    elif attempt == 2:
        B = str(input("Re-enter the password:"))
        while B != A:
            B = str(input("Wrong! Please enter the correct password again:"))
        A = str(input("Enter a new password between 6-8 characters:"))
        while len(A) > 8 or len(A) < 6:
            A = str(input("Password must be between 6-8 characters. Enter a new password:"))
        print("Password change has been successful")
getPword(attempt)