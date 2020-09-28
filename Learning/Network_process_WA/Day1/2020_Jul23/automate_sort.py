from subprocess import Popen, PIPE

sort_command = Popen("sort", stdout=PIPE, stdin=PIPE, encoding="utf8")

while True:
    line = input("Enter a line: ")
    if not line: break
    sort_command.stdin.write(line + "\n")

sort_command.stdin.close()

for line in sort_command.stdout:
    print(line)