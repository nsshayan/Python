commands = [
        {"program": "ftp ftp.chandrashekar.info",
         "commands": [
                     ("Name .*: ", "testuser"),
                     ("Password: ", "w3lc0me"),
                     ("ftp> ", ["cd /www/files", "get test.txt", "quit"])
                 ]
        },
]

def run_commands(c):
    pass # TODO

if __name__ == '__main__':
    run_commands(commands)
