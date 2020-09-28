from flask import Flask

app = Flask("my_app")

def connect_to_server():
    from pssh.clients import SSHClient

    conn = SSHClient("192.168.56.101", user="root", password="welcome")
    return conn




@app.route("/mem/<pid>")
def get_mem_usage(pid):
    c = connect_to_server()
    channel, host, stdout, stderr, stdin = c.run_command(f"grep ^Vm /proc/{pid}/status")
    lines = ""
    for line in stdout:
        lines += line
    return lines

if __name__ == '__main__':
    app.run(debug=True)

