from subprocess import Popen
#p = Popen(["ls", "/etc", ">", "ls.out"], shell=True)

# Replacement for os.system()
#ret = Popen("ls /etc; date; whoami; cd /; ls", shell=True).wait()
#ret = Popen("ls sdlkfjlsdf", shell=True).wait()
from time import sleep

p = Popen("./slow_script.sh")
for i in range(5):
    print("Python program: counting", i)
    sleep(1)

#print("Waiting for script to finish...")
#ret = p.wait()
#print("script complete: ret =", ret)

print("Terminating script...")
#p.kill()
#p.send_signal(15)
import signal
p.send_signal(signal.SIGQUIT)

print("script killed...")
