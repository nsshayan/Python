import subprocess

try:
    r = subprocess.run(["./testscript.py"], check=True, timeout=3)

except subprocess.CalledProcessError as e:
    print("Command failed: e =", e)

except subprocess.TimeoutExpired as e:
    print("Command timeout: e =", e)

else:
    print("Command completed successfully.")
    print(r)
    print(r.returncode, r.args)
