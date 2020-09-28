home_page = "http://testing.chandrashekar.info/"
login_url = "http://testing.chandrashekar.info/wp-login.php"
username = "testuser"
password = 'w3lc0me'
dashboard_url = "http://testing.chandrashekar.info/wp-admin/"
add_new_posts_url = "http://testing.chandrashekar.info/wp-admin/post-new.php"

from mechanicalsoup import StatefulBrowser
import sys

browser = StatefulBrowser()
r = browser.open(login_url)
assert r.ok and browser.get_url() == login_url

loginform = browser.select_form("#loginform")
browser["log"] = username
browser["pwd"] = password
r = browser.submit_selected()
assert r.ok and browser.get_url() == dashboard_url

r = browser.follow_link(text="Add New")
assert r.ok and browser.get_url() == add_new_posts_url

post_form = browser.select_form("#post")
browser["post_title"] = input("Enter blog title: ")
print("Enter blog content below. Press Ctrl-d to complete.")
print("---------------------------------------------------")
browser["content"] = sys.stdin.read()

publish_btn = browser.get_current_page().select("input#publish")[0]

r = browser.submit_selected(publish_btn)
assert r.ok and browser.get_current_page().select("div#message p")[0].text == "Post published"
