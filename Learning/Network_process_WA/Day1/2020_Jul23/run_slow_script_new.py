from subprocess import Popen, run, TimeoutExpired, CalledProcessError
from time import sleep

try:
    out = run("./slow_script.sh", timeout=15, check=True)
except TimeoutExpired as e:
    print("Timeout occurred: ", e)
except CalledProcessError as e:
    print("Program failed:", e)
else:
    print("out = ", out)
    print("program was", out.args)
    print("program exit code: ", out.returncode)

print("main program exiting....")