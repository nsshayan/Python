from subprocess import Popen, PIPE
#with Popen("ls", stdout=PIPE, universal_new_lines=True) as p: # Python 3.2 to 3.5

#with Popen("ls", stdout=PIPE, encoding="utf8") as p:  # Python 3.6 or above
#    for line in p.stdout:
#        print(line)

# This works for all versions from Python 3.0
with Popen("ls", stdout=PIPE) as p:
    for line in p.stdout:
        print(str(line, "utf8"))
