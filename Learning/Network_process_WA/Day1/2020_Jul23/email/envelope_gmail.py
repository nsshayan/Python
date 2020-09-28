from envelopes import Envelope, GMailSMTP

envelope = Envelope(
    from_addr=('scary.pythonista@gmail.com', 'A Scary Pythonista'),
    to_addr=('joe@chandrashekar.info', 'Joe Smith'),
    subject='Envelopes demo from Gmail account',
    text_body="this is a test message from a Python program."
)
envelope.add_attachment('/Users/chandrashekar/Documents/python-logo.png')

# Send the envelope using an ad-hoc connection...
#envelope.send('smtp.googlemail.com', login='from@example.com',
#              password='password', tls=True)

# Or send the envelope using a shared GMail connection...
gmail = GMailSMTP('scary.pythonista@gmail.com', 'slashprog')
r = gmail.send(envelope)
print(r)


