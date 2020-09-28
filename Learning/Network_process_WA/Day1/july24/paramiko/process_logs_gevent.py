from gevent import monkey
monkey.patch_all()

import gevent

ssh_info = [
        ("192.168.56.101", {
                "username": "root",
                "password": "welcome",
                "logfiles": ["/var/log/system.log", "/var/log/pacman.log"]
                }),

        ("192.168.56.101", {
                "username": "root",
                "password": "welcome",
                "logcommands": ["/usr/bin/dmesg", "/usr/bin/journalctl"]

                })

 ]

#from queue import Queue
#queue = Queue(1000)

from gevent.queue import Queue
queue = Queue(1000)

greenlets = []

def ssh_connect(host, username, password):
    from paramiko import SSHClient, AutoAddPolicy
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(host, username=username, password=password)
    return client


def run_command(client, command):
    channel = client.get_transport().open_channel("session")
    channel.exec_command(command)
    stream = channel.makefile("r")
    for line in stream:
        queue.put({command: line})

def parse_log(client, logfile):
    #channel = client.get_transport().open_channel("session")
    #channel.exec_command("cat {}".format(logfile))
    #stream = channel.makefile("r")
    # for line in stream:
    #    queue.put(line)

    sftp = client.open_sftp()
    with sftp.open(logfile, "r") as log:
        for line in log:
            queue.put({logfile: line})

def create_connection(host, info):

    ssh_client = ssh_connect(host,
                             info["username"],
                             info["password"])
    if "logfiles" in info:
        for logfile in info["logfiles"]:
            #th = Thread(target=parse_log, args=(ssh_client, logfile))
            #th.start()
            th = gevent.spawn(parse_log, ssh_client, logfile)
    elif "logcommands" in info:
        for command in info["logcommands"]:
            #th = Thread(target=run_command, args=(ssh_client, command))
            #th.start()
            th = gevent.spawn(run_command, ssh_client, command)

    greenlets.append(th)

def process_logs(ssh_info):

    for host, info in ssh_info:

        #conn_thread = Thread(target=create_connection,
        #                    args=(info,))
        #conn_thread.start()
        #connections.append(conn_thread)
        conn_thread = gevent.spawn(create_connection, host, info)
        greenlets.append(conn_thread)

    while True:
        line = queue.get()
        print(line)

    gevent.joinall(greenlets)


if __name__ == '__main__':
    process_logs(ssh_info)
