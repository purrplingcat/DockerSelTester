# DockerSelTester
Selenium tester environment in Docker

## Install & Run

```
$ git clone https://github.com/EllenFawkes/DockerSelTester.git
$ docker build -t yourCompany/selenium .
$ docker run -v /your/test/dir:/tests --rm yourCompany/selenium
```

## Writing tests

Write your selenium tests with python and Selenium library. For better work, you can use internal class `SeleniumTestCase' (included in this docker image).

#### Example

```python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys, unittest, time, re, datetime
from SeleniumTestCase import SeleniumTestCase

class LoginLogoutTest(SeleniumTestCase):

    def test_login_logout(self):
        self.base_url = "http://example.com/adminclient/"
        driver = self.driver
        driver.get(self.base_url + "")
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//div[@id='adminclient-36241446']/div/div[2]/div/div/div/div").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("#gwt-uid-3").clear()
        driver.find_element_by_css_selector("#gwt-uid-3").send_keys("admin")
        driver.find_element_by_id("gwt-uid-5").clear()
        driver.find_element_by_id("gwt-uid-5").send_keys("admin")
        driver.find_element_by_xpath("//div[@id='adminclient-36241446']/div/div[2]/div/div/div/div/div[5]/div").click()
        for i in range(60):
            try:
                if u"Odhlásit" == driver.find_element_by_css_selector("div.v-button.v-widget").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//div[@id='adminclient-36241446']/div/div[2]/div/div/div/div/div[3]/div").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//div[@id='adminclient-36241446']/div/div[2]/div/div/div/div").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(u"Přihlásit", driver.find_element_by_xpath("//div[@id='adminclient-36241446']/div/div[2]/div/div/div/div/div[5]/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

if __name__ == "__main__":
    unittest.main()
```
