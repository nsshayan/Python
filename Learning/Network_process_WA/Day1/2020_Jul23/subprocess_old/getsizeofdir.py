from subprocess import Popen, PIPE
import re

def replace_spaces(s):
    pattern = re.compile("\s+")
    return pattern.sub(" ", s)
  
    
p = Popen("ls -l", stdout=PIPE, shell=True)

total = 0
for line in p.stdout:
    line = replace_spaces(line)
    if len(line.split(" ")) > 3:
       total += int(line.split(" ")[4])  
p.wait()
print(total)

