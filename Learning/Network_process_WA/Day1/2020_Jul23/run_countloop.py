from subprocess import Popen, PIPE

command = Popen("./countloop.sh", stdout=PIPE)

for line in command.stdout:
    print(line.upper())
    
