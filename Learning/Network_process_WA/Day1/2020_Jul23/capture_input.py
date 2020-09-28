from subprocess import Popen

with open("run_commands.txt", "rb") as infile:
    with Popen("python", stdin=infile) as p:
        p.wait()
