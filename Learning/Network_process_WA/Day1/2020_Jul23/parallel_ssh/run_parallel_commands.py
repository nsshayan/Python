from pssh.utils import load_private_key
from pssh.clients import ParallelSSHClient

host_config = {'192.168.56.104' : {
                        'user': 'root',
                        'password': 'welcome',
                        'port': 22,
                        }
              }

hosts = list(host_config.keys())

client = ParallelSSHClient(hosts * 4, host_config=host_config)
output = client.run_command('%s', host_args=["uptime", "whoami", "date", "uname -a"])
for host, host_output in output.items():
    for line in host_output.stdout:
        print(host, line)
