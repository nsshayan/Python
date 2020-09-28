
def extract_output(command, regex):
    from subprocess import Popen, PIPE
    import re
    import shlex
    pattern = re.compile(regex, re.VERBOSE | re.DOTALL | re.MULTILINE)
    with Popen(shlex.split(command), encoding="utf8", stdout=PIPE) as p:
        for line in p.stdout:
            for m in pattern.finditer(line):
                yield m

if __name__ == '__main__':
    ipaddr_regex = r"\d{1,3}(\.\d{1,3}){3}"

    for match in extract_output("/sbin/ifconfig", ipaddr_regex):
        print(match.group())