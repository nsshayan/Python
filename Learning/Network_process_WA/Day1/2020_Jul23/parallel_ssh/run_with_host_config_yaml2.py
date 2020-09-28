from pssh.utils import load_private_key
from pssh.clients import SSHClient
import yaml


with open("host_config.yml") as yaml_file:
    host_config = yaml.load(yaml_file, Loader=yaml.CLoader)

clients = []
for host, info in host_config.items():
    client = SSHClient(
        host=host,
        port=info["port"],
        user=info["user"],
        password=info["password"])
    for command in info["commands"]:
        output = client.run_command(command)
        clients.append(output)

print(clients)
for channel, host, stdout, stderr, stdin in clients:
    for line in stdout:
        print(host, line)
