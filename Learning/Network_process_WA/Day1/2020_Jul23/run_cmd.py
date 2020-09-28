from subprocess import Popen, DEVNULL
from shlex import split

if __name__ == '__main__':
    command = split(input("Enter command: "))
    ret = Popen(command,
                stdout=DEVNULL,
                stdin=DEVNULL,
                stderr=DEVNULL
                ).wait()
    if ret == 0:
        print("Success")
    else:
        print("Failed with exit code", ret)
