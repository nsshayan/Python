from __future__ import print_function
import sys
if sys.version_info.major < 3:
    input = raw_input

from subprocess import Popen
from shlex import split

while True:
    comm = input("Enter command: ")
    if not comm: break
    try:
        ret = Popen(split(comm)).wait()
    except OSError as e:
        print("Failed to launch program:", e)
    else:
        print("Return value:", ret)

