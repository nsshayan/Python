from subprocess import Popen, PIPE

#p = Popen(["ls",  "-l"], stdout=PIPE, encoding="utf8")

p = Popen(["ls",  "-l"], stdout=PIPE, universal_newlines=True)
print("ls command launched: p =", p)

for line in p.stdout:
    print(line.upper())

exit_code = p.wait()
print("ls command exited: exit code =", exit_code)
