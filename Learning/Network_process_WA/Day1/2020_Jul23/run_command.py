
def run_command(command, capture_output_for=None):
    from subprocess import Popen, PIPE
    import shlex
    if capture_output_for:
        import re
        pattern = re.compile(capture_output_for)

    command = Popen(shlex.split(command),
                    stdout=PIPE,
                    encoding="utf8")
    for line in command.stdout:
        if capture_output_for:
            matches = pattern.finditer(line)
            if matches:
                for m in matches:
                    yield m.group()
        else:
            yield line.strip()


if __name__ == '__main__':
    for line in run_command("ls"):
        print(line)

    regex = r"\d+(\.\d+){3}"
    for value in run_command("ifconfig", capture_output_for=regex):
        print(value)
