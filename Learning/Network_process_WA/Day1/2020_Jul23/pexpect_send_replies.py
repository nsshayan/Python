import pexpect
from collections import OrderedDict
from random import choice

replies = OrderedDict([
        ("name", ["john", "jane", "joe", "adam", "bourne"]),
        ("time", ["11:00:00", "14:00:00", "5:30:00", "19:00:00"]),
        ("live", ["pune", "kolkatta", "delhi", "mumbai"]),
        ("long", ["12", "3", "9", "20", "45", "-3", "14"])
])

greeter = pexpect.spawn("./random_greeter.py", encoding="utf8")
prompts = list(replies.keys())

while True:
    i = greeter.expect(prompts)
    reply = choice(replies[prompts[i]])
    print(greeter.before + greeter.after, reply)
    greeter.sendline(reply)


