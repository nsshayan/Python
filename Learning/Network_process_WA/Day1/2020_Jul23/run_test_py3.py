from subprocess import run, CalledProcessError

try:
    ret = run(["ls", "/bin"], check=True)
except CalledProcessError as e:
    print("*** Caught exception:", e)
else:
    print("ret =", ret)
