from subprocess import Popen

with open("./testfolder/testfile.txt", "rb") as infile, \
     open("./testfolder/testfile.out", "wb") as outfile:
    r = Popen("sort", stdin=infile, stdout=outfile).wait()

