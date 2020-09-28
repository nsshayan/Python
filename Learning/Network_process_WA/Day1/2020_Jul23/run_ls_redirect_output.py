from subprocess import Popen

with open("ls.out", "w") as outfile:
    process = Popen("ls", stdout=outfile)
    
ret = process.wait()
print("ls complete...")