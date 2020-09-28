from subprocess import Popen, PIPE

wc = Popen("wc", stdout=PIPE, stdin=PIPE, encoding="utf8")

data = """
sdj flks jklfs jdlkj sdlkf
eworu oiwe uroiwu roiweu roiweu
lksjfklj sdlkf jsdklf jsdklf
iwue rioweuroi uwior
ldklfjlksdjflsdjflksj flksj ld
kld jfkljdsfklsjdfl
"""
wc.stdin.write(data)
wc.stdin.close()

for line in wc.stdout:
    lines, words, chars = line.split()
wc.wait()
print("Number of lines: {}, Number of words: {}, Number of characters: {}".format(
    lines, words, chars))
print("--- done ---")
