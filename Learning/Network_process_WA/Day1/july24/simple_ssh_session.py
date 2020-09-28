from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())

client.connect(hostname="dhrona.net", 
               port=12276,
               username="user1",
               password="welcome")

shell = client.invoke_shell()

stdin = shell.makefile_stdin("w")
stdout = shell.makefile("r")
stderr = shell.makefile_stderr("r")

stdin.write("uname -a\n")
print(stdout.readline())
print(stdout.readline())
print(stdout.readline())


stdin.close()
stdout.close()
stderr.close()
shell.close()
client.close()
