from sys import argv
from robobrowser import RoboBrowser

def assert_response_ok(browser):
    if not browser.response.ok:
        print("*** Failed request on:", browser.url)
        print("*** Response code:", browser.response.status_code )
        exit(1)

if len(argv) < 2:
    print("usage: {} search_keyword.".format(argv[0]))
    exit(1)

search = argv[1]

browser = RoboBrowser(parser="lxml", history=True)
browser.open('http://pypi.python.org/')
assert_response_ok(browser)

form = browser.get_form(action='/pypi')
form['term'] = search
browser.submit_form(form)

list_of_entries = browser.select('table.list tr td a')[:5]
for link in list_of_entries:
	print(link.text, "-----", link["href"])


