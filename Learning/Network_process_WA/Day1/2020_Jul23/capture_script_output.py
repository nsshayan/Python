from subprocess import Popen, PIPE
from time import ctime

with Popen("./slow_script.sh", stdout=PIPE, encoding="utf8") as p:
    for line in p.stdout:
        print(f"{ctime()}: {line.upper()}")
