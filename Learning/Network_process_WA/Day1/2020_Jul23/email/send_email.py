#!/usr/bin/env python
from smtplib import SMTP

from_addr = "testuser@chandrashekar.info"
to_list = ["joe@chandrashekar.info", "chandrashekar.babu@gmail.com"]

data = """
From: Chandrashekar <testuser@chandrashekar.info>
Subject: April 12th 2017 - Test email!
Cc: Chandrashekar Babu <chandrashekar.babu@gmail.com>

This is a dummy message
slkfsklfjsdklfsd
flskjf ksdljflsdf
dsflksd jfklsdjfsd
fdskl fjsdklfjsdf
"""

mail = SMTP("mail.chandrashekar.info", 587)
mail.set_debuglevel(7)
mail.ehlo_or_helo_if_needed()
mail.login("testuser", "w3lc0me")

mail.sendmail(from_addr, to_list, data)
