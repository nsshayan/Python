#!/usr/bin/env python

from time import ctime

with open(f"/tmp/test-program-{ctime()}.tmp", "w") as outfile:
        outfile.write("A dummy file created...\n")
