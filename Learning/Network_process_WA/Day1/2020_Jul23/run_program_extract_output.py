
def program_output(command, regex_patterns):
    from subprocess import Popen, PIPE
    import re
    import shlex

    for k, v in regex_patterns.items():
        regex_patterns[k] = re.compile(v)

    args = shlex.split(command)

    with Popen(args, stdout=PIPE, encoding="utf8") as p:
        for line in p.stdout:
            for k, pattern in regex_patterns.items():
                for m in pattern.finditer(line):
                    yield k, m

if __name__ == '__main__':
    for key, match in program_output("/sbin/ifconfig",
                                {
                                    "ipv4_addr": r"\d{1,3}(\.\d{1,3}){3}",
                                    "mac_addr": r"[0-9a-f]{2}(:[0-9a-f]{2}){5}"
                                }):

        print(key, match.group())