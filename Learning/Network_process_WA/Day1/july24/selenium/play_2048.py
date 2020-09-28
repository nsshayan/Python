from itertools import cycle

url = "https://gabrielecirulli.github.io/2048/"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get(url)


elem = driver.find_element_by_class_name("game-container")

for key in cycle([Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]):
    elem.send_keys(Keys.UP)

driver.close()
