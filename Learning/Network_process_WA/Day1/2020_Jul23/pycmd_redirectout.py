from subprocess import Popen
import rlcompleter
import shlex

while True:
    outfile = None

    command = input("PyCmd> ")
    if command == "exit": 
        break
    args = shlex.split(command)

    # Check for output redirection
    if ">" in args:
        filename = args[args.index(">") + 1]
        args.remove(">")
        args.remove(filename)
        outfile = open(filename, "wb")

    # Check for output redirection
    if ">>" in args:
        filename = args[args.index(">>") + 1]
        args.remove(">>")
        args.remove(filename)
        outfile = open(filename, "ab")

    #ret = Popen(command.split()).wait()
    #ret = Popen(shlex.split(command)).wait()
    ret = Popen(args, stdout=outfile).wait()
    print("ret = ", ret)    

