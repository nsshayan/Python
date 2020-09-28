from subprocess import Popen, PIPE


def get_ip_addr():

    with Popen("ifconfig", stdout=PIPE, encoding="utf8") as p:
        # for line in p.stdout:
        #    if "inet " in line:
        #        print(line.split()[1])
        ipaddrs = [line.split()[1] for line in p.stdout if "inet " in line]
    return ipaddrs


print(get_ip_addr())
