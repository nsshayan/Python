from subprocess import Popen, PIPE

                        #, universal_new_lines=True
with Popen(["ls", "-l"], stdout=PIPE, encoding="utf8") as p:
    for line in p.stdout:
        print(line, end="")
