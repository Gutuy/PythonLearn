correctpassword="admin123"
Password=input("Enter the password:")
while Password!=correctpassword:
    print("Incorrect password. Please try again.")
    Password=input("Enter the password:")

    print("Access granted. Welcome!")