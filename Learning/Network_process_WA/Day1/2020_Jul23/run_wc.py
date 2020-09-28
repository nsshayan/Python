from subprocess import Popen, PIPE

data = """
js dlkfjkls jfklsdj fklsdj fklsdj kfldsj f
ow ioweu rioweu ioweu iro weuiow euir
sdlk fklsdj lksdj fklsd jfklsj fkljsd fklsdjf
dl jflkdsfj lksd fjklsd jfklsd jfklsd jfklsdjf
dslk kdslj fklsd jfklsd jfklsd jfsd jfksdjkfl sdjf
sdjf sd jfklsdj fksdj f
"""

wc_command = Popen("wc", stdin=PIPE)
wc_command.stdin.write(data)
wc_command.stdin.close()
wc_command.wait()


