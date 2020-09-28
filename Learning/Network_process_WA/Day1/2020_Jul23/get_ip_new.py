from subprocess import Popen, PIPE

def get_ip_addr_macos():
    command = "/sbin/ifconfig"
    # For Python 3.3 to 3.5
    # with Popen(command, stdout=PIPE, universal_new_lines=True) as proc:

    # For python 3.6+
    with Popen(command, stdout=PIPE, encoding="utf8") as proc:
        #for line in proc.stdout:
        #    if "inet " in line:
        #        print(line.split()[1])
        return [ line.split()[1] for line in proc.stdout if "inet " in line ]

def get_ip_addr_windows():
    command = "ipconfig"
    with Popen(command, stdout=PIPE, encoding="utf8") as proc:
        return [line.split()[-1] for line in proc.stdout if "IPv4" in line]


if __name__ == '__main__':
    print(get_ip_addr_macos())
