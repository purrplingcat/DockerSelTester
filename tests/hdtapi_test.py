# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time
import re


def click_on_window(self, x, y, name="Firefox"):
    # inicialize xdotool
    xdo = Xdo()
    # get id of tiger vnc
    if name:
        val = xdo.search_windows(name.encode('ascii'))
        # move on coordinates
        xdo.move_mouse(int(x), int(y))
        # focus on window and click
        xdo.click_window(val[0], 1)
    else:
        self.log.error("No window to click.")


class Hdtapi(unittest.TestCase):

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException:
            return False

    def setUp(self):
#	chrome_options = webdriver.ChromeOptions()
#	chrome_options.add_argument('--no-sandbox')
#	self.driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
	self.driver = webdriver.Firefox()
	self.driver.implicitly_wait(20)
        self.base_url = "http://lajka:8002"
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_hdtapi(self):
        driver = self.driver
        # driver.find_element_by_name("Log In").click()
        driver.get(self.base_url + "/tree/")
        driver.find_element_by_link_text("ComponentsConfig").click()
        driver.find_element_by_link_text("Per4manceConfig").click()
        driver.find_element_by_link_text("Save").click()
        driver.find_element_by_link_text("Home").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
