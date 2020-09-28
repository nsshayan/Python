from pssh.utils import load_private_key
from pssh.clients import ParallelSSHClient

host_config = {'192.168.56.105' : {'user': 'root', 'password': 'welcome',
                          'port': 22,
                          #'private_key': load_private_key(
                          #  'my_key.pem')
                              },
               'dhrona.net' : {'user': 'user1', 'password': 'welcome',
                          'port': 12276,
                          #'private_key': load_private_key(
                          #    open('my_other_key.pem'))
                              },
              }
hosts = list(host_config.keys()) + (["192.168.56.105"] * 5)
print(hosts)

client = ParallelSSHClient(hosts, host_config=host_config)
commands = ("uptime", "whoami", "date", "uname", "id", "hostname", "pwd")

#output = client.run_command('%s', host_args=commands)
#output = client.run_command("whoami")
dirs = ("one", "two", "three", "four", "five", "six", "seven")
output = client.run_command('mkdir /tmp/%s', host_args=dirs)

for host, host_output in output.items():
    for line in host_output.stdout:
        print(host, line)
