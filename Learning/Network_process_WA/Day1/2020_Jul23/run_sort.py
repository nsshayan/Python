from subprocess import Popen

with open("names.txt") as infile, \
     Popen("sort", stdin=infile) as sort_proc:
        pass
