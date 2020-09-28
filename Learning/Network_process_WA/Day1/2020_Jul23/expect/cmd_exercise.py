"""
Implement a skeleton command shell.

"""

# Call this function if input is 'list'
def listdir(): print("Listing directory")

# Call this function if input is 'whoami'
def show_user(): print("root")

# Call this function if input is 'date'
def curr_date(): print("Jan 10 2014")

# Call this function if input is anything else
def invalid_cmd(): print("Invalid command")

# Call this function if input is 'exit'
def exit_program(): exit(0)


while True:
    cmd = input("Cmd> ")
    # Implement the logic here.
