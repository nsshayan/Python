from subprocess import Popen

print("Running ls command...")
#child_process = Popen("ls /usr/bin")
child_process = Popen(["ls", "/usr/bin"])

print("ls command running: ", child_process)

ret = child_process.wait()
print("ls command complete. ret =", ret)
