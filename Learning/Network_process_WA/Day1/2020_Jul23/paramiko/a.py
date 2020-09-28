#!/usr/bin/env python

print("This is a dummy python program...")
with open("/proc/cpuinfo") as infile:
    for line in infile:
        print(line.strip())

