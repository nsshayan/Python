from mechanicalsoup import StatefulBrowser

home_url = "http://testing.chandrashekar.info/"

username = "testuser"
password = "w3lc0me"

login_url = "http://testing.chandrashekar.info/wp-login.php"

logged_in_url = "http://testing.chandrashekar.info/wp-admin/"

add_new_post_url = "http://testing.chandrashekar.info/wp-admin/post-new.php"

browser = StatefulBrowser()

browser.open(login_url)
assert browser.get_url() == login_url

browser.select_form()
browser["log"] = username
browser["pwd"] = password
browser.submit_selected()
assert browser.get_url() == logged_in_url
print(browser.get_url())

browser.follow_link("post-new.php")
assert browser.get_url() == add_new_post_url
print(browser.get_url())


