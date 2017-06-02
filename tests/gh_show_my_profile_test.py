# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ShowMyProfile(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://github.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_show_my_profile(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Sign in").click()
        driver.find_element_by_id("login_field").clear()
        driver.find_element_by_id("login_field").send_keys("ellenfawkes")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("******")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_xpath("//ul[@id='user-links']/li[3]/a").click()
        driver.find_element_by_link_text("Your profile").click()
        try: self.assertTrue(driver.find_element_by_xpath("//img[contains(@src,'https://avatars3.githubusercontent.com/u/4710267?v=3&s=460')]").is_displayed())
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(driver.find_element_by_css_selector("div.js-pinned-repos-reorder-container").is_displayed())
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Ellen Fawkes", driver.find_element_by_css_selector("span.vcard-fullname.d-block").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
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
