import re
import shlex
from subprocess import Popen, PIPE

def parse_output(command, regex):
    pattern = re.compile(regex)
    with Popen(shlex.split(command), 
               stdout=PIPE, encoding="utf8") as p:
        
        for line in p.stdout:
            for m in pattern.finditer(line):
                yield m
            
if __name__ == '__main__':
    for ipaddr in parse_output("/sbin/ifconfig", 
                               r'(\d{1,3})(\.\d{1,3}){3}'):
        print("IP: ", ipaddr.group())
