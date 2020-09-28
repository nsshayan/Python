from subprocess import run, CalledProcessError, TimeoutExpired

try:
    #result = run(["ls", "-l", "/werewr"], check=True, timeout=3, encoding="utf8")
    result = run("./slow_script.sh", check=True, timeout=3, encoding="utf8")
except CalledProcessError as e:
    print("Command failed: e =", e)
except TimeoutExpired:
    print("Timed out!!!")
else:
    print("Command success: r =", result.returncode)
