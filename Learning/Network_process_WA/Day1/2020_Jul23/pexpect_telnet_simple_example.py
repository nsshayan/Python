import pexpect

outfile = open("transcript.log", "w")

with pexpect.spawn("telnet 192.168.56.104 2023",
                    encoding="utf8",
                    logfile=outfile) as conn:
    conn.expect("login: ")
    conn.sendline("pythonista")



    while True:
        conn.expect("Password: ")
        p = input("Enter password: ")
        conn.sendline(p)
        r = conn.expect(["\[pythonista@archvm ~\]\$", "Login incorrect.+login: "], timeout=5)
        if r == 0:
            break
        elif r == 1:
            print("Wrong password")
            conn.sendline("pythonista")

    print("Login successful.")
    conn.sendline("uptime")
    conn.expect("\[pythonista@archvm ~\]\$")
    print(conn.before)

outfile.close()
