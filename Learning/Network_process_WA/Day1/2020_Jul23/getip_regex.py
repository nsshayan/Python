

def parse_output(command, regex):
    from subprocess import Popen, PIPE
    import re
    import shlex

    pattern = re.compile(regex, re.VERBOSE | re.DOTALL)

    with Popen(shlex.split(command),
               stdout=PIPE,  # encoding='utf8',
               universal_newlines=True) as p:

        for line in p.stdout:
            matches = pattern.finditer(line)
            if matches:
                for m in matches:
                    yield m


if __name__ == '__main__':
    ip_regex = "\d{1,3}(\.\d{1,3}){3}"

    for match in parse_output("ifconfig", ip_regex):
        print(match.group())
