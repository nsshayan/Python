from pssh.clients import SSHClient

client = SSHClient(host="192.168.56.105", user="root", password="welcome")

script = """
import sys
print(sys.version_info)
exit()
"""

ch, host, stdout, stderr, stdin = client.run_command("python",
                                                    use_pty=True)

stdin.write(script)


for line in stderr:
    print(line)

for line in stdout:
    print(line)

stdin.close()
