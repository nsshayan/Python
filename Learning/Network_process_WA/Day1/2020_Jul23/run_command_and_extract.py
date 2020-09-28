from subprocess import Popen, PIPE


def run_command(command, regex):
    import re
    pattern = re.compile(regex)

    with Popen(command, stdout=PIPE, encoding="utf8") as proc:
        for line in proc.stdout:
            for m in pattern.finditer(line):
                if m:
                    yield m


for match in run_command("ifconfig", "\d{1,3}(\.\d{1,3}){3}"):
    print(match.group())
