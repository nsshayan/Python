from pssh.clients import SSHClient

 client = SSHClient(host="192.168.56.105", user="root", password="welcome")

 ch, host, stdout, stderr, stding = client.run_command("uptime")
 for line in stdout:
     print(line)