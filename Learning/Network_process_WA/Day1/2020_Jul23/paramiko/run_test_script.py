def connect_ssh(hostname, username, password):
    from paramiko import SSHClient, AutoAddPolicy

    import logging
    logging.basicConfig(filename="run_bc.log")
    log = logging.getLogger("paramiko")
    log.setLevel(logging.DEBUG)

    ssh_client = SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())

    ssh_client.connect(hostname, username=username, password=password)

    return ssh_client

if __name__ == '__main__':
    ssh = connect_ssh("192.168.56.101", "root", "welcome")
    #stdin, stdout, stderr = ssh.exec_command('./test_script.sh')
    #print(stdout.readline())

    #stdin.write(commands)

