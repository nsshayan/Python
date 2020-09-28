"""
Simulate the shell command 'ls -l | wc -l'
using subprocess module
"""
from subprocess import Popen, PIPE

ls_command = Popen(["ls", "-l"], stdout=PIPE)

wc_command = Popen(["wc", "-l"],
                   stdin=ls_command.stdout)




