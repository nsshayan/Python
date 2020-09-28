from subprocess import Popen, PIPE
import re

regex = r"\d{1,3}(\.\d{1,3}){3}"
pattern = re.compile(regex)

ifconfig = Popen("ifconfig", stdout=PIPE, universal_newlines=True)

for line in ifconfig.stdout:
    #match = pattern.search(line)
    matches = pattern.finditer(line)
    if matches:
        for match in matches:
            print(match.group())
        
    