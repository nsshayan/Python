from subprocess import Popen, PIPE

with Popen(["ls", "-l"],
           stdout=PIPE, # encoding='utf8',
           universal_newlines=True) as p:
    for line in p.stdout:
        print(line.strip().upper())
