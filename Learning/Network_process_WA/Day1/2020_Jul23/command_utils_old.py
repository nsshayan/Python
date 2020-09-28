def run_command(command, extract):
    from subprocess import Popen, PIPE
    import shlex
    import re

    for pattern_name, regex in extract.items():
        extract[pattern_name] = re.compile(regex)

    #results = []
    with Popen(shlex.split(command), stdout=PIPE, encoding="utf8") as p:
        for line in p.stdout:
            for name, pattern in extract.items():
                match = pattern.search(line)
                if match:
                    yield {name: match}

        #return results
