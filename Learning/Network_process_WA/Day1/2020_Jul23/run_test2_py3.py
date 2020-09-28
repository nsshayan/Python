from subprocess import run

ret = run("./slow_script.sh", timeout=5)
