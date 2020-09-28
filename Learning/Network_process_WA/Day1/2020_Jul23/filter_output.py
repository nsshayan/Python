
def filter_output(program, regex):
    from subprocess import Popen, PIPE
    import re

    pattern = re.compile(regex)
    with Popen(program, stdout=PIPE, universal_newlines=True) as process:
        for line in process.stdout:
            matches = pattern.finditer(line)
            if matches:
                for match in matches:
                    yield match


if __name__ == '__main__':
    ipv4_regex = r"\d{1,3}(\.\d{1,3}){3}"
    for m in filter_output("ifconfig", ipv4_regex):
        print(m.group())
