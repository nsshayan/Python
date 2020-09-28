from subprocess import Popen

with open("commands.lst") as commands:
    for line in commands:
        print("======== Launching command: {} =====".format(line))
        comm = line.split()
        ret = Popen(comm).wait()
        print(">>>>>>>> command returned {} <<<<<<<".format(ret))


