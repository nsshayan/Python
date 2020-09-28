from subprocess import Popen, PIPE

def get_ipv4_addr_old():
    p = Popen("/sbin/ifconfig", stdout=PIPE, encoding="utf8")
    for line in p.stdout:
        if "inet " in line:
            print(line.split()[1])

def get_ipv4_addr():
    with Popen("/sbin/ifconfig", stdout=PIPE, encoding="utf8") as p:
        return [ line.split()[1] \
                 for line in p.stdout \
                 if "inet " in line ]


def get_ipv4_addr_re():
    import re
    ipv4_regex = r"(\d{1,3}\.){3}\d{1,3}"
    pattern = re.compile(ipv4_regex)
    with Popen("ifconfig", stdout=PIPE, encoding="utf8") as p:
        for line in p.stdout:
            for match in  pattern.finditer(line):
                print(match.group())

#get_ipv4_addr_re()

def run_command(command :str, extract :dict):
    import re
    import shlex

    #extract_patterns = {}
    #for k, v in extract.items():
    #    extract_patterns[k] = re.compile(v)

    extract_patterns = { k: re.compile(v) for k, v in extract.items() }

    with Popen(shlex.split(command), stdout=PIPE, encoding="utf8") as p:
        for n, line in enumerate(p.stdout):
            for key, pattern in extract_patterns.items():
                for match in  pattern.finditer(line):
                    yield n, key, match


for n, key, match in run_command("ifconfig",
                          {
                              "ipv4_addresses": r"(\d{1,3}\.){3}\d{1,3}"
                          }):
    print(n, key, match.group(), match.span())
