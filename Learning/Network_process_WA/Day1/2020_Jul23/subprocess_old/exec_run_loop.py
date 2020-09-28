import subprocess

with open("/dev/null", "w") as out, open("/dev/null") as infile:
    ret = subprocess.call(["python", "run_loop.py"], close_fds=True,
                           stdin=infile, stdout=out)


#print "Control back to main program..."

#p = subprocess.Popen(["python", "run_loop.py"])
#p.wait()

print("Control back to main program...")
#from time import sleep
#i = 0
#while True:
#    print "Counting in main program: ", i
#    i += 1
#    sleep(1)


