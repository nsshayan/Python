def run(command, patterns):
    import re
    for key, value in patterns.items():
        patterns[key] = re.compile(value)
    
    from subprocess import Popen, PIPE
    import shlex
    with Popen(shlex.split(command), stdout=PIPE, encoding="utf8") as p:
        for line in p.stdout:
            for key, pattern in patterns.items():
                for match in pattern.finditer(line):
                    yield key, match             
    

if __name__ == '__main__':
    for key, match in run("ifconfig", {"ipv4_addr": "\d{1,3}(\.\d{1,3}){3}"}):

        print(key, match.group())


