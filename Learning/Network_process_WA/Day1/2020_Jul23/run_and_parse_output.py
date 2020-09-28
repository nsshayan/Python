def run_command(command, regex_string):
    from subprocess import Popen, PIPE
    import shlex
    import re

    pattern = re.compile(regex_string,
                         re.VERBOSE | re.MULTILINE)

    with Popen(shlex.split(command),
               stdout=PIPE,
               encoding="utf8") as proc:

        for line in proc.stdout:
            for match in pattern.finditer(line):
                yield match


def run_command_into_list(command, regex_string):
    from subprocess import Popen, PIPE
    import shlex
    import re

    result = []
    pattern = re.compile(regex_string, re.VERBOSE | re.MULTILINE)

    with Popen(shlex.split(command), stdout=PIPE, encoding="utf8") as proc:

        for line in proc.stdout:
            for match in pattern.finditer(line):
                result.append(match)

    return result