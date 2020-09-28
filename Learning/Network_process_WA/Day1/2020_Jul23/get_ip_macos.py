from subprocess import Popen, PIPE
from time import ctime

def get_ip_addresses_old():
    with Popen("/sbin/ifconfig", stdout=PIPE, encoding="utf8") as p:
        for line in p.stdout:
            if "inet " in line:
                print(line.split()[1])

def get_ip_addresses_rigid():
    with Popen("/sbin/ifconfig", stdout=PIPE, encoding="utf8") as p:
        ipaddrs = [ line.split()[1] \
                    for line in p.stdout \
                        if "inet " in line ]
    return ipaddrs

def get_ip_addresses():
    import re

    pattern = re.compile(r"\d{1,3}(\.\d{1,3}){3}")
    ipaddrs = []

    with Popen("/sbin/ifconfig", stdout=PIPE, encoding="utf8") as p:
        for line in p.stdout:
            for m in pattern.finditer(line):
                ipaddrs.append(m.group())
    return ipaddrs


def run_command_output_list(command, regex):
    import re
    import shlex

    pattern = re.compile(regex)
    result = []

    with Popen(shlex.split(command), stdout=PIPE, encoding="utf8") as p:
        for line in p.stdout:
            for m in pattern.finditer(line):
                result.append(m.group())
    return result


def run_command_output(command, regex):
    import re
    import shlex

    pattern = re.compile(regex)

    with Popen(shlex.split(command), stdout=PIPE, encoding="utf8") as p:
        for line in p.stdout:
            for m in pattern.finditer(line):
                yield m



print(get_ip_addresses())