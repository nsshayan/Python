# Exercise: Implement this program

ssh_info = [
    {   "hostname": "192.168.56.101",
        "port": 22,
        "username": "root",
        "password": "welcome",
        "commands": [
            "uptime",
            "uname -a",
            "date" ]
    },

    {   "hostname": "192.168.56.102",
        "port": 22,
        "username": "root",
        "password": "welcome",
        "commands": [
            "cat /etc/passwd",
            "cat /proc/loadavg",
            "uptime" ]
    },
]

    def parse_logs(server_info):
        pass

if __name__ == '__main__':
    parse_logs(ssh_info)
