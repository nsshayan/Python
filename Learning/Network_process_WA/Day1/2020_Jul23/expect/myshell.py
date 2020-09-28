#!/usr/local/bin/python3

prompt = "PyShell> "
while True:
    c = input(prompt)
    if c in ["aaa", "bbb", "ccc"]:
        prompt = ">>> "
    elif c in ["ddd", "eee", "fff"]:
        prompt = "*** "
    elif c in ["exit", "quit"]:
        break
    else:
        prompt = "PyShell> "

    print("Got", c)


