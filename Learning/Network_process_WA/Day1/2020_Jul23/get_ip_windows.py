from subprocess import Popen, PIPE

def get_ip():
    ipconfig = Popen("ipconfig", stdout=PIPE)
    return [ str(line.split()[-1], "utf8")  \
             for line in ipconfig.stdout   \
             if b"IPv4 " in line ]

ip_addresses = get_ip()
print(ip_addresses)
                     
                     


