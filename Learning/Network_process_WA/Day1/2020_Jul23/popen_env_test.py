from subprocess import Popen

#Popen("/bin/bash", env=dict(PATH="/bin:/usr/bin", NAME="john")).wait()
Popen("./env_test.py", env=dict(PATH="/bin:/usr/bin", NAME="john")).wait()