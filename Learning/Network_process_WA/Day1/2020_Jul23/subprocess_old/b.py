from subprocess import Popen, PIPE

outfile = open("ls.out", "w")

p = Popen("ls", stdout=outfile)

p.wait()

