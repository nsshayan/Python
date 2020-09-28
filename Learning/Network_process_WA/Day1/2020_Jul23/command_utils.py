def run_command(command, patterns):
    from subprocess import Popen, PIPE
    import shlex
    import re

    for key, value in patterns.items():
        patterns[key] = re.compile(value, re.VERBOSE)

    with Popen(shlex.split(command), stdout=PIPE, encoding="utf8") as proc:
        for line in proc.stdout:
            for key, pattern in patterns.items():
                for m in pattern.finditer(line):
                    yield {key: m}
