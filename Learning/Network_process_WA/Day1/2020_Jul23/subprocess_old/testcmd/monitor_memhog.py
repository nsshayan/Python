from subprocess import Popen, PIPE
from time import sleep

ps_command = "ps -aeo pid,rss".split()

p = Popen("./mem_hog.py")
pid = bytes(str(p.pid), "utf8")

while True:
    ps = Popen(ps_command, stdout=PIPE)
    for line in ps.stdout:
        fields = line.split()
        if pid == fields[0]:
            print("\r{}                      ".format(str(line.strip(), "utf8")), end="")
    sleep(2)

