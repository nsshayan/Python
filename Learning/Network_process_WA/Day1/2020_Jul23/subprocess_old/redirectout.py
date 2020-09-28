import sys

old = sys.stdout

sys.stdout = open("/dev/pts/7", "w")
print("Hello world")
print("sdkfjdlksjflksdjf lksd jfsdf")

sys.stdout = old
print("done")

