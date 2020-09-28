from subprocess import Popen, PIPE


def get_ip_addr():
    with Popen("ifconfig", stdout=PIPE, encoding="utf8") as p:
        #for line in p.stdout:
        #    if "inet " in line:
        #        print(line.split()[1])
        return [line.split()[1] for line in p.stdout if "inet " in line]


print(get_ip_addr())
