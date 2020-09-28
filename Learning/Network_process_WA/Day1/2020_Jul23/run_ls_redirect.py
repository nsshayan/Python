from subprocess import Popen

with open("ls.out", "w") as outfile:
    p = Popen(["ls", "-l"], encoding="utf8", stdout=outfile)
    print("Launched ls command: p =", p)
    exit_code = p.wait()

print("ls command finished: exit_code =", exit_code)
