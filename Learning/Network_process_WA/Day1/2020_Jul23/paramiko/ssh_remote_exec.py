ssh_config = {

    "192.168.56.101": {
        "username": "root",
        "password": "welcome",
        "commands": [
            {
                "run": "uname -a",
                "stdout": "./uname.out"
            },
            {
                "run": "ls -l /usr /sdfsf /boot"
                "stdout": "./ls.out",
                "stderr": "./ls.err"
            }
        ]
    },

    "192.168.56.102": {
        "username": "root",
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

