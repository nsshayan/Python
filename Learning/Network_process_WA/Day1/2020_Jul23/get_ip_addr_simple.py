from subprocess import Popen, PIPE

def get_ipv4_addr():
    with Popen("ifconfig", stdout=PIPE, encoding="utf8") as p:
        ipv4_addrs = [ line.split()[1] \
                       for line in p.stdout \
                       if "inet " in line]
    return ipv4_addrs

if __name__ == '__main__':
    print(get_ipv4_addr())
    