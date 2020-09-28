from subprocess import Popen

Popen("ls", cwd="/usr").wait()