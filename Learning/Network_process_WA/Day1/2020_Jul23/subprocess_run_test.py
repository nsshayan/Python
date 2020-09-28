import subprocess


try:
    ret = subprocess.run("./simple_loop.sh", check=True, timeout=5)
except subprocess.CalledProcessError as e:
    print("Command failed: e =", e)
except subprocess.TimeoutExpired as e:
    print("Timeout occurred")
else:
    print("Command completed: ret =", ret.returncode)
