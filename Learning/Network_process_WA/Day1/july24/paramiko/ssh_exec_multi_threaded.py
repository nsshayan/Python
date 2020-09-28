from threading import Thread
from queue import Queue

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

def run_command(client, hostname, command, queue):
    stdin, stdout, stderr = client.exec_command(command)
    def getoutput(stream, msg):
        for line in stream:
            output = (hostname, command, msg, line)
            queue.put(output)
    out_thread = Thread(target=getoutput, args=(stdout, "stdout"))
    err_thread = Thread(target=getoutput, args=(stderr, "stderr"))
    out_thread.start()
    err_thread.start()

def ssh_run(ssh_info):
    from paramiko import SSHClient, AutoAddPolicy
    output = Queue(4096)
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
        for command in info["commands"]:
            Thread(target=run_command, args=(client,
                                            info["hostname"],
                                            command,
                                            output)).start()

    return output

if __name__ == '__main__':

    output = ssh_run(ssh_info)
    while True:
        data = output.get()
        print(data)