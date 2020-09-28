from subprocess import Popen

#p = Popen("ls | wc -l", shell=True)  # sh -c "ls | wc -l"

#p = Popen("ls -l /usr")

p = Popen(["ls", "-l", "/usr"])