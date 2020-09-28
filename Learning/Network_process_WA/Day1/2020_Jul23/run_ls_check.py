from subprocess import run, CalledProcessError
from time import sleep

try:
    ret = run("ls /", shell=True, check=True)
except CalledProcessError as e:
    print("Failed: e =", e)
else:
    print(f"ls command completed, args = {ret.args}, exit code = {ret.returncode}")
