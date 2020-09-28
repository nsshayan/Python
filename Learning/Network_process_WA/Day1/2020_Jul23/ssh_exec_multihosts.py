# Exercise: Implement this program
# Connect to multiple hosts as per the
# ssh_info configuration list provided as
# argument to ssh_run() function, run commands
# and capture outputs and make it available to the
# main code.

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

def ssh_run(ssh_info):
    pass # TODO: Implement the logic here.

if __name__ == '__main__':
    for host, result in ssh_run(ssh_info):
        for command, stdin, stdout, stderr in result:
            print(f"host: {host}, command: {command}")
            for line in stdout:
                print(line)
            print("-" * 60)
