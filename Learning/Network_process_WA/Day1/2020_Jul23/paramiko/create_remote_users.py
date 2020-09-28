import paramiko

import logging
logging.basicConfig(filename="run_ls.log")
log = logging.getLogger("paramiko")
log.setLevel(logging.DEBUG)

#key = paramiko.RSAKey(data=base64.decodestring('AAA...'))
#client.get_host_keys().add('ssh.example.com', 'ssh-rsa', key)

client = paramiko.SSHClient()
# client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.set_missing_host_key_policy(paramiko.RejectPolicy())
# client.set_missing_host_key_policy(paramiko.WarningPolicy())

#from getpass import getpass
#password = getpass("Enter password: ")

#password = "welcome"

user_details = {
    "abc": "welcome",
    "xyz": "welcome123",
    "aaabbccc": "test456"
}

user_add = "useradd -m {username}"

client.connect('192.168.56.101', username="root")

for name, passwd in user_details.items():
    stdin, stdout, stderr = client.exec_command(user_add.format(username=name))
    for line in stdout:
        print("out: ", line)
    print("-" * 40)

    stdin, stdout, stderr = client.exec_command("passwd " + name)
    stdin.write(passwd + "\r\n")
    stdin.write(passwd + "\r\n")
    stdin.close()
    for line in stdout:
        print("out2: ", line)
    print("=" * 40)


client.close()
