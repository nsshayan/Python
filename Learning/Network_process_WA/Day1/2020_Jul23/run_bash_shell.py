from subprocess import Popen
import os

environment = os.environ.copy()
environment.update({"NAME": "Sam", "ROLE": "Admin"})
p = Popen("bash", cwd="/opt", env=environment)
p.wait()
print("bash exited...")