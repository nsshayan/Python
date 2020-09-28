def run_command(command):
    from subprocess import Popen, PIPE
    with Popen(command, stdout=PIPE, encoding="utf8") as p:
        for line in p.stdout:
            yield line

def parse_output(command, regex_string):
    import re
    pattern = re.compile(regex_string)

    for line in run_command(command):
        for match in pattern.finditer(line):
            yield match.group()

if __name__ == '__main__':
    for ipaddr in parse_output("/sbin/ifconfig", r'(\d{1,3})(\.\d{1,3}){3}'):
        print("IP: ", ipaddr)
