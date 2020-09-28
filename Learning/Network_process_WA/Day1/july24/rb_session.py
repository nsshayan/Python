# coding: utf-8
from robobrowser import RoboBrowser
b = RoboBrowser(parser="lxml")
b.open("http://testing.chandrashekar.info/wp-login.php")
b.url
login_form = b.get_form()

login_form["log"] = "pythonista"
login_form["pwd"] = "w3lc0me"

b.submit_form(login_form)
b.url
