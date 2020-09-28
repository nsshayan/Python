
def ssh_connect(host, username, password=None, logfile=None):
    from paramiko import SSHClient, AutoAddPolicy

    if logfile:
        import logging
        logging.basicConfig(filename=logfile)
        log = logging.getLogger("paramiko")
        log.setLevel(logging.DEBUG)

    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())

    ssh_client.connect(host, username=username, password=password)

    return ssh_client

def ssh_close(ssh_client):
    ssh_client.close()
    