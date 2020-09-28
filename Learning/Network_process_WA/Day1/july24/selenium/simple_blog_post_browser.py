# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://testing.chandrashekar.info/wp-login.php?loggedout=true")
        driver.find_element_by_id("user_login").click()
        driver.find_element_by_id("user_login").clear()
        driver.find_element_by_id("user_login").send_keys("pythonista")

        driver.find_element_by_id("user_pass").clear()
        driver.find_element_by_id("user_pass").send_keys("w3lc0me")

        driver.find_element_by_id("wp-submit").click()

        driver.find_element_by_link_text("Add New").click()
        
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("a simple test message")
        driver.find_element_by_id("content").clear()
        driver.find_element_by_id("content").send_keys("ksdfjksdj fklsdjfklsd jfkls djlfk jsdlkf jsdklf jsdlkfs")
        driver.find_element_by_id("publish").click()
        driver.find_element_by_link_text("View post").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
