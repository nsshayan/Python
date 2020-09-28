from ssh_connection import SSHConnection


with SSHConnection("192.168.56.101", "root", "welcome") as conn:
    conn.put("a.py", "/tmp/a.py")
    conn.chmod("/tmp/a.py", 0o755)
    stdin, stdout, stderr = conn.exec_command("/tmp/a.py")
    print(str(stdout.read(), "utf8"))
    conn.get("/etc/passwd", "localfile.txt")
