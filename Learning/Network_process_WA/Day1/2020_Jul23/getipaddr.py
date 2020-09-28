from subprocess import Popen, PIPE

with Popen("ifconfig",
           stdout=PIPE,  # encoding='utf8',
           universal_newlines=True) as p:
    for line in p.stdout:
        if "inet " in line:
            print(line.split()[1])

        # if "IPv4 address" in line:
        #    print(line.split()[-1])
