from subprocess import Popen, PIPE

bc_commands = """
scale=2000
sqrt(2)
"""

calc = Popen(["bc", "-l"], stdin=PIPE, stdout=PIPE, universal_newlines=True)
#calc.stdin.write(bc_commands)
#calc.stdin.flush()

output, error = calc.communicate(input=bc_commands)
print(output)
calc.wait()
