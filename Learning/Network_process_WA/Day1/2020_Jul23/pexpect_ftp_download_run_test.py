import pexpect

ftp_events = [
    ("Name.+:", "testuser"),
    ("Password:", "w3lc0me"),
    ("ftp>", "cd /www/files"),
    ("ftp>", "get xml.zip"),
    ("ftp>", "quit")
]

pexpect.run("ftp ftp.chandrashekar.info", events=ftp_events)

    