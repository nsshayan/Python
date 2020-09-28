from subprocess import Popen, PIPE
def get_ip_addr():
    command = ["/sbin/ifconfig | grep inet | grep -v inet6"]
    ipaddresses = []
    with Popen(command, stdout=PIPE, encoding="utf8",shell=True) as p:
        for line in p.stdout:
            ip = line.split('NETMASK')
            print(ip)
            #ipaddresses.append(ip)
    return ipaddresses
if __name__ == '__main__':
    print(get_ip_addr())
    # OUT: ["192.168.1.28", "127.0.0.1"]
