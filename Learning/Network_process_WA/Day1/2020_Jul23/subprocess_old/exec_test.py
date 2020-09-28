import os

print("This is python program...")
os.execv("/bin/ls", ["/bin/ls", "/"])
print("Back to python program...")

