from subprocess import Popen, PIPE
with open("ls.out", "wb") as outfile:
    # proc = Popen(["ls", "-l"], stdout=PIPE) # Python 2.x
    with Popen(["ls", "-l"], stdout=PIPE) as proc:
        for line in proc.stdout:
            print(line)
            outfile.write(line)