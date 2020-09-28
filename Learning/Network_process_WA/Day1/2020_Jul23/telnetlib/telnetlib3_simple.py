import asyncio, telnetlib3

@asyncio.coroutine
def shell(reader, writer):
    buf = ''
    while True:
        outp = yield from reader.read(1024)
        if not outp:
            # EOF
            return

        print(outp, end='', flush=True)

        if '?' in outp:
            # reply all questions with 'y'.
            writer.write('y')

    print()

loop = asyncio.get_event_loop()
coro = telnetlib3.open_connection('localhost', 6023, shell=shell)
reader, _ = loop.run_until_complete(coro)
loop.run_until_complete(reader.protocol.waiter_closed)

