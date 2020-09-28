from subprocess import Popen

#Popen("/bin/bash", env={"NAME": "dsfljsdfds", "VALUE": "oweurewr"}).wait()
Popen("./show_env.py", env={"NAME": "dsfljsdfds", "VALUE": "oweurewr"}).wait()
# Popen("./show_env.py").wait()
