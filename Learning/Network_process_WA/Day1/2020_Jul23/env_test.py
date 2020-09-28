from subprocess import Popen

ret = Popen("./child_process.py", env={"MYNAME": "Chandrashekar"}).wait()
