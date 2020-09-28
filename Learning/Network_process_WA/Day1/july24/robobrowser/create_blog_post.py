from robobrowser import RoboBrowser
from sys import stdin

def assert_response(br, url):
    if not br.response.ok or br.url != url:
        print("Request failed:", br.response.status_code)
        print("URL =", br.url)
        exit(1)

browser = RoboBrowser(parser="lxml")

browser.open("http://www.chandrashekar.info/user/login")
assert_response(browser, "http://www.chandrashekar.info/user/login")

login_form = browser.get_form(id="user-login")

login_form["name"] = "testuser"
login_form["pass"] = "w3lc0me"
browser.submit_form(login_form)
assert_response(browser, "http://www.chandrashekar.info/user/16")
print("Logged in!")

link = browser.get_link("View recent blog entries")
browser.follow_link(link)
assert_response(browser, "http://www.chandrashekar.info/blog/16")
print("Viewing blog entries...")

link = browser.get_link("Post new blog entry.")
browser.follow_link(link)
assert_response(browser, "http://www.chandrashekar.info/node/add/blog")
print("Posting new blog entries")

blog_form = browser.get_form(id="blog-node-form")

#title = input("Enter blog title")
#print("Enter blog contents/body below:\n---------------------------")
#body = stdin.read()

title = "another test blog via robobrowser"
body = "kds fjlksdj flksd jflk sdklf sdklf jsdklfj dsklfj skdlf jklsd jflks jflksd fklsd jfs"

blog_form["title"] = title
blog_form["body[und][0][summary]"] = body
blog_form["body[und][0][value]"] = body

submit_field = blog_form.submit_fields["op"]
submit_field.value = "Save"
browser.submit_form(blog_form, submit_field)

#browser.submit_form(blog_form, blog_form.submit_fields["op"])
if not browser.url.startswith("http://www.chandrashekar.info/node/"):
    print("Failed to add new blog: URL =", browser.url)

print("Blog available at ", browser.url)


