from multiprocessing import Process
from selenium.webdriver import Firefox, Safari, Chrome

browsers = [Firefox, Safari, Chrome]

def run_session(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("python")
    driver.find_element_by_id("tsf").submit()
    driver.find_element_by_xpath(
        "//div[@id='rso']/div/div/div/div/a/h3").click()
    driver.find_element_by_link_text("Python Docs").click()
    driver.find_element_by_link_text("Library Reference").click()
    driver.find_element_by_link_text(
        u"sqlite3 — DB-API 2.0 interface for SQLite databases").click()


def run_browser(Driver):
    driver = Driver()
    print("driver = ", driver)
    run_session(driver)
    driver.close()

workers = []
for b in browsers:
    t = Process(target=run_browser, args=(b,))
    t.start()
    workers.append(t)
