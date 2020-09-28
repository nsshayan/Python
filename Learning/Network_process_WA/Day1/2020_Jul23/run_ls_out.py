from subprocess import Popen

#p = Popen("ls -l", shell=True)
with open("ls.out", "w") as outfile:
    p = Popen(["ls",  "-l"], stdout=outfile)
    print("ls command launched: p =", p)
    exit_code = p.wait()
print("ls command exited: exit code =", exit_code)
