from subprocess import Popen, PIPE
import re
import shlex

def parse_command_output(command, extract):
    # compile extraction patterns
    for k, regex in extract.items():
        extract[k] = re.compile(regex, re.VERBOSE)

    args = shlex.split(command)
    with Popen(args, stdout=PIPE, encoding="utf8") as proc:
        for line in proc.stdout:
            for k, pattern in extract.items():
                for match in pattern.finditer(line):
                    yield k, match
