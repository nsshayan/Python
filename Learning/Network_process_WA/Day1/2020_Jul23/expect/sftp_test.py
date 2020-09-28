import ssh
t = ssh.Transport(("localhost", 22))
t.connect(username="chandras", password="welcome")
sftp = ssh.SFTPClient.from_transport(t)
sftp.listdir()
sftp.put("README", "README")
sftp.put("/Users/chandrashekar/contact.txt", "README")
sftp.listdir()
