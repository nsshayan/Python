from subprocess import Popen

with open("bc.input", "rb") as infile, \
     open("bc.result", "wb") as outfile:    
    Popen("bc", stdin=infile, stdout=outfile).wait()

with open("bc.input", "r") as infile, \
     open("bc.result", "r") as resultfile:
     for expression, result in zip(infile, resultfile):
         print(f"{expression.strip()} = {result.strip()}")

