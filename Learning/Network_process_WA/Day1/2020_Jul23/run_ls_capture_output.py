from subprocess import Popen, PIPE
                                   
p = Popen("ls", stdout=PIPE, encoding="utf8") # 3.6+
                            # universal_new_lines=True) # 3.2 to 3.5
for line in p.stdout:
    print("line: ", line)