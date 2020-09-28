def ssh_connect(host, username, password):
    from paramiko import SSHClient, AutoAddPolicy

    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(host, username=username, password=password)
    return client

def exec_command(client, command):
    channel = client.invoke_shell()
    stdin = channel.makefile_stdin("w")
    stdout = channel.makefile("r")
    stderr = channel.makefile_stderr("r")
    stdin.write(command)
    return stdin, stdout, stderr


if __name__ == '__main__':
    client = ssh_connect("192.168.56.105", "root", "welcome")
    stdin, stdout, stderr = client.exec_command("ls -l /usr/local")

    for line in stdout:
        print(line)

    client.close()
