"""
Implement the ssh_remote_exec() function that connects
to multiple servers as per the keys in ssh_config, and
executes commands and allows capturing their output.


"""

ssh_config = {

    "dhrona.net": {
        "port": 12276,
        "username": "user1",
        "password": "welcome",
        "commands": [
            {
                "run": "uname -a",
                "stdout": "./uname.out"
            },
            {
                "run": "ls -l /usr /sdfsf /boot",
                "stdout": "./ls.out",
                "stderr": "./ls.err"
            }
        ]
    },

    "dhrona.net": {
        "port": 12276,
        "username": "user2",
        "password": "welcome",
        "commands": [
            {
                "run": "uptime",
                "stdout": "./uptime.out"
            }
        ]
    }
}

def ssh_remote_exec(config):
    pass # TODO: Implement this function


if __name__ == '__main__':
    ssh_remote_exec(ssh_config)

