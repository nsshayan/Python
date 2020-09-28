from subprocess import Popen

#p = Popen(["ls", "-l", "*.py"])

#p = Popen("ls -l *.py", shell=True)
p = Popen("ls")

p.wait()

