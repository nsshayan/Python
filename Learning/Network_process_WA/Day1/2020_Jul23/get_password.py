import getpass

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

print(f"Username {username}, Password is {password}")
print("Logged in as", getpass.getuser())
