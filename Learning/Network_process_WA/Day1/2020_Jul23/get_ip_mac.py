from subprocess import Popen, PIPE

def get_ip():
    ifconfig = Popen("ifconfig", stdout=PIPE)
    return [ str(line.split()[1], "utf8")  \
             for line in ifconfig.stdout   \
             if b"inet " in line ]

ip_addresses = get_ip()
print(ip_addresses)
                     
                     


