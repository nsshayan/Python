from mechanicalsoup import StatefulBrowser

browser = StatefulBrowser()

browser.open("http://www.python.org/")

browser.follow_link("/blogs/")
#browser.follow_link(text="Python News")
print(browser.get_url())

browser.select_form()
browser.get_current_form().print_summary()

browser["q"] = "Raymond Hettinger"
browser.submit_selected()

print(browser.get_url())
print("-" * 40)
print(browser.links())
browser.close()
