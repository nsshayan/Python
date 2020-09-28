# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest

class PostBlogTestCase(unittest.TestCase):
    def setUp(self):
        from selenium import webdriver
        self.driver = webdriver.Firefox()

    def test_login_page(self):
        driver = self.driver
        driver.get("http://www.chandrashekar.info/user/login")
        self.assertTrue(self.is_element_present(By.ID, "page-title"))
        self.assertTrue(self.is_element_text(By.ID, "page-title", "USER LOGIN"))

        driver.find_element_by_id("edit-name").click()
        driver.find_element_by_id("edit-name").clear()
        driver.find_element_by_id("edit-name").send_keys("testuser")
        driver.find_element_by_id("edit-pass").click()
        driver.find_element_by_id("edit-pass").clear()
        driver.find_element_by_id("edit-pass").send_keys("w3lc0me")
        driver.find_element_by_id("edit-submit").click()

        self.assertTrue(self.is_element_present(By.ID, "page-title"))
        self.assertTrue(self.is_element_text(By.ID, "page-title", "TESTUSER"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "View recent blog entries"))

        driver.find_element_by_link_text("View recent blog entries").click()
        self.assertTrue(self.is_element_present(By.ID, "page-title"))
        self.assertTrue(self.is_element_text(By.ID, "page-title", "TESTUSER'S BLOG"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Post new blog entry."))


        driver.find_element_by_link_text("Post new blog entry.").click()
        self.assertTrue(self.is_element_present(By.ID, "page-title"))
        self.assertTrue(self.is_element_text(By.ID, "page-title", "CREATE BLOG ENTRY"))

        driver.find_element_by_id("edit-title").click()
        driver.find_element_by_id("edit-title").clear()
        driver.find_element_by_id("edit-title").send_keys("test blog - chandrashekar - December 01")
        driver.find_element_by_id("edit-body-und-0-value").clear()
        driver.find_element_by_id("edit-body-und-0-value").send_keys("this is a test message .\nslkdfjlksdjfsd\nfsdkljfsd\nfsdlkfj sdkljf sdfsdflksdj fkljsdflkjsdlkfjsdklfj sdlkfsd\nfsdlfj lskdfjklsjfl")
        driver.find_element_by_id("edit-submit").click()

        self.assertTrue(self.is_element_present(By.LINK_TEXT, "test blog - chandrashekar - December 01"))

    def element_text_contains(self, how, what, text):
        try:
            return text in self.driver.find_element(by=how, value=what).text
        except NoSuchElementException as e:
            return False

    def is_element_text(self, how, what, text):
        try:
            return self.driver.find_element(by=how, value=what).text == text
        except NoSuchElementException as e:
            return False

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        else:
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

if __name__ == "__main__":
    unittest.main()
