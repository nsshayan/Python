from __future__ import print_function

from subprocess import Popen, PIPE
import re
re_pattern = r"""
   inet
   \s+
   ([\d\.]+)
   .+
   (
     broadcast
     \s+
     ([\d\.]+)
    )?
"""
pattern = re.compile(re_pattern, re.VERBOSE)

p = Popen("ifconfig", stdout=PIPE)
for line in p.stdout:
    #if b"inet " in line:
    #    print(line.split()[1])
    match = pattern.search(str(line, "utf8"))
    #match = re.search(re_pattern, str(line, "utf8"), re.VERBOSE)
    if match:
        print(match.group(1), match.group(3))
ret = p.wait()

# https://public.etherpad-mozilla.org/p/Advanced_Python