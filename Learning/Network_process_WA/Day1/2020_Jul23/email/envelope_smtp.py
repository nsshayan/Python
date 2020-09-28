from envelopes import Envelope

envelope = Envelope(
    from_addr=('testuser@chandrashekar.info', 'Test User'),
    to_addr=('joe@chandrashekar.info', 'Joe Smith'),
    subject='Envelopes demo',
    text_body="this is a test string"
)

envelope.add_attachment('/Users/chandrashekar/Documents/python-logo.png')

r = envelope.send(
        host="mail.chandrashekar.info",
        port=587,
        login="testuser@chandrashekar.info",
        password="w3lc0me",
        tls=True
)

print(r)
