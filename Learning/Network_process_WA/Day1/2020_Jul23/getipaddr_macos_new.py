from subprocess import Popen, PIPE

def get_ip_macos():
    with Popen("/sbin/ifconfig", stdout=PIPE, encoding="utf8") as p:
        return [ line.split()[1] for line in p.stdout if "inet " in line ]

    #for line in p.stdout:
    #    if "inet " in line:
    #        print(line.split()[1])

if __name__ == '__main__':
    print(get_ip_macos())