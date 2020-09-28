from subprocess import Popen
environment = {"A": "100", "NAME": "A test program"}
from os import environ

ret = Popen("bash", cwd="/", env=dict(environ, **environment)).wait()
print("Shell exited with return code: ", ret)
