
def get_ip_address():
    from subprocess import Popen, PIPE
    p = Popen("ifconfig", stdout=PIPE)
    return [ str(line.split()[1], "utf8") for line in p.stdout if b"inet " in line ]
    #return [ line.split()[1] for line in Popen("ifconfig", stdout=PIPE).stdout if b"inet " in line ]


print(get_ip_address())

