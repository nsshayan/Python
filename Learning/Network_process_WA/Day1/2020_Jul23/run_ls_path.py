from subprocess import Popen
from shlex import quote

path = input("Enter path: ")

command = "ls -l {}"

ret = Popen(command.format(quote(path)), shell=True).wait()

