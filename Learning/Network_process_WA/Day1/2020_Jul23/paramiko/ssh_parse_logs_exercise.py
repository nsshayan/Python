# Exercise: Implement this program

ssh_info = {
    "192.168.56.101": {
        "username": "root",
        "password": "welcome",
        "logfiles": ["/var/log/pacman.log", "/var/log/system.log"]
    },

    "192.168.56.102": {
        "username": "pythonista",
        "password": "welcome",
        "logcommands": ["/usr/bin/dmesg", "/usr/bin/journalctl"]

    }

}

def parse_logs(server_info):
        pass

if __name__ == '__main__':
    parse_logs(ssh_info)
