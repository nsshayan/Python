def run_command(command :str, extract :dict):
    import re
    import shlex
    from subprocess import Popen, PIPE

    extract_patterns = { k: re.compile(v) for k, v in extract.items() }

    with Popen(shlex.split(command), stdout=PIPE, encoding="utf8") as p:
        for n, line in enumerate(p.stdout):
            for key, pattern in extract_patterns.items():
                for match in  pattern.finditer(line):
                    yield n, key, match
