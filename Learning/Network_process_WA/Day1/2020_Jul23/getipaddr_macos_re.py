from subprocess import Popen, PIPE
import re

ipv4_regex = r"\d{1,3}(\.\d{1,3}){3}"
ipv4_pattern = re.compile(ipv4_regex)

p = Popen("ifconfig",
          #universal_newlines=True,
          encoding="utf8",
          stdout=PIPE)

for line in p.stdout:
    for m in ipv4_pattern.finditer(line):
        print(m.group())


