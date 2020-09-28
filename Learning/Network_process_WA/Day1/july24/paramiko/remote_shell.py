from gevent import monkey; monkey.patch_all()

#import rlcompleter
from threading import Thread

def ssh_connect(host, port=22, username=None, password=None):
    from paramiko import SSHClient, AutoAddPolicy
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(host, port, username=username, password=password)
    return client

def create_shell(client):
    channel = client.invoke_shell()
    stdin = channel.makefile("w")
    stdout = channel.makefile("r")
    stderr = channel.makefile_stderr("r")
    return stdin, stdout, stderr

def read_input(out):
    while True:
        user_input = input("SSH> ")
        if user_input == "exit":
            out.close()
            break
        out.write(user_input + "\n")
        out.flush()

def get_server_output(handle):
    for line in handle:
        print(line, end="", flush=True)

if __name__ == '__main__':
    cl = ssh_connect("192.168.56.104", username="root", password="welcome")
    stdin, stdout, stderr = create_shell(cl)

    # read_input(stdin)
    stdin_thread = Thread(target=read_input, args=(stdin,))
    stdout_thread = Thread(target=get_server_output, args=(stdout,))
    stderr_thread = Thread(target=get_server_output, args=(stderr,))

    stdin_thread.start()
    stdout_thread.start()
    stderr_thread.start()

    stdin_thread.join()
    stdout_thread.join()
    stderr_thread.join()
    cl.close()
