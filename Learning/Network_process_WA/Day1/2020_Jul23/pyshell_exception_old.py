from subprocess import check_call, CalledProcessError
import readline
from shlex import split

if __name__ == '__main__':
    while True:
        command = input("PyShell> ")
        #ret = Popen(command.split()).wait()
        try:
            ret = check_call(split(command))
        except CalledProcessError as e:
            print("Command failed with: ", e)
        else:
            print("Ret =", ret)
