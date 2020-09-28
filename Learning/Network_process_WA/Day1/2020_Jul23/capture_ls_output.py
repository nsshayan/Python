from subprocess import Popen

with open("lsoutput.log", "wb") as outfile:
    with Popen(["ls", "-l", "/usr"], stdout=outfile) as p:
        p.wait()
        
    