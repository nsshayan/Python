import pexpect


# Tuple-set
shell_session = [
    ([">>> ", "PyShell> ", "\*\*\*"], "exit\r"),
]

commands = ["test\r", "hello\r", "world\r", "aaa\r"]


def getvalue(* args):
    # print(args)
    return commands.pop(0)


shell_session_dict = {
    ">>> ": "ddd\r",
    "PyShell> ": getvalue,
    "\*\*\* ": "exit\r"
}
with open("shell.log", "wb") as log:
    pexpect.run("./myshell.py",
                events=shell_session_dict,
                logfile=log)
