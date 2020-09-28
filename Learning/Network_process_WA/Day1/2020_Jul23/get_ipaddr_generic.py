def parse_command_output(command, regex):
    from subprocess import Popen, PIPE
    import shlex
    import re
    pattern = re.compile(regex, re.VERBOSE | re.DOTALL)
    with Popen(shlex.split(command), stdout=PIPE, encoding="utf8") as p:
        for line in p.stdout:
            for match in pattern.finditer(line):
                yield match

if __name__ == '__main__':

    ip_regex = r"""
        (\d{1,3})     # Match first octet (e.g. aaa of aaa.bbb.ccc.ddd )
        (\.\d{1,3}){3}  # Match next 3 octets preceded by . ( .bbb.ccc.ddd )
    """
    for result in parse_command_output(
                        command="/sbin/ifconfig",
                        regex=ip_regex):
        print(result.group())
