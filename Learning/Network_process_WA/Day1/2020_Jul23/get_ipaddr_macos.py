from subprocess import Popen, PIPE
command = "/sbin/ifconfig"

def get_ip_addr():
    with Popen(command, stdout=PIPE, encoding="utf8") as p:
        #for line in p.stdout:
        #    if "inet " in line:
        #        print(line.split()[1])
        return [ line.split()[1] for line in p.stdout if "inet " in line ]

if __name__ == '__main__':

    print(get_ip_addr())
    # OUT: ["192.168.1.28", "127.0.0.1"]
