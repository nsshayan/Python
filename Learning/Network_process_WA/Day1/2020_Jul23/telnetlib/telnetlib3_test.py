import asyncio, telnetlib3

@asyncio.coroutine
def shell(reader, writer):
    commands = ["uname -a", "ls /usr/local", "exit"]
    while commands:
        outp = yield from reader.read(1024)
        if not outp:
            # EOF
            return

        print(outp, end='', flush=True)

        if '?' in outp:
            # reply all questions with 'y'.
            writer.write('y')

        if "login:" in outp:
            writer.write("root\n")

        if "Password:" in outp:
            writer.write("welcome\n")

        if "[root@archvm]# " in outp:
            c = commands.pop(0)
            writer.write(c + "\n")

    print()

loop = asyncio.get_event_loop()
coro = telnetlib3.open_connection('192.168.56.101', 23, shell=shell)
reader, _ = loop.run_until_complete(coro)
#loop.run_until_complete(reader.waiter_closed)

