from subprocess import Popen, DEVNULL

child = Popen(["ls", "-l"], stdout=DEVNULL, stderr=DEVNULL)
child.wait()
