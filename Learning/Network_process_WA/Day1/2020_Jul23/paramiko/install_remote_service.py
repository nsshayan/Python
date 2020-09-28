import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('192.168.56.101', username="root", password="welcome")

sftp = client.open_sftp()

my_startup_script_contents = """#!/usr/bin/env python
print("Hello world from python!")

"""

rc_local_service_contents = """
# /etc/systemd/system/my-startup.service
[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/lib/systemd/my-startup-script

[Install]
WantedBy=multi-user.target
"""

with sftp.open("/etc/systemd/system/my-startup.service", "w") as out:
    out.write(rc_local_service_contents)

with sftp.open("/usr/lib/systemd/my-startup-script", "w") as out:
    out.write(my_startup_script_contents)

sftp.chmod("/usr/lib/systemd/my-startup-script", 0o755)

client.exec_command("systemctl enable my-startup.service")

sftp.close()
client.close()
