from subprocess import Popen

with open("bc_input.txt") as bc_input, open("bc_output.txt", "w") as out:
    p = Popen("bc", stdin=bc_input, stdout=out)

p.wait()


