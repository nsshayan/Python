
ssh_info = [
    {   "hostname": "192.168.56.105",
        "port": 22,
        "username": "root",
        "password": "welcome",
        "commands": [
            "uptime",
            "uname -a",
            "date" ]
    },

    {   "hostname": "dhrona.net",
        "port": 12276,
        "username": "user1",
        "password": "welcome",
        "commands": [
            "cat /etc/passwd",
            "cat /proc/loadavg",
            "uptime" ]
    },
]

def ssh_run(ssh_info):
    from paramiko import SSHClient, AutoAddPolicy
    output = []
    for info in ssh_info:
        client = SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(
                 hostname=info["hostname"],
                 port=info["port"],
                 username=info["username"],
                 password=info["password"])
        #ssh_args = dict(info.items() - dict(commands=info["commands"]).items())
        #client.connect(**ssh_args)
        result = []
        for command in info["commands"]:
            stdin, stdout, stderr = client.exec_command(command)
            result.append((command, stdin, stdout, stderr))
        output.append((info["hostname"], result))

    return output

if __name__ == '__main__':
    for host, result in ssh_run(ssh_info):
        for command, stdin, stdout, stderr in result:
            print(f"host: {host}, command: {command}")
            for line in stdout:
                print(line)
            print("-" * 60)
