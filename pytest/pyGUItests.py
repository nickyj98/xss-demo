from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
import time
import hashlib
import requests
import random, string
import pytest
import os 


@pytest.fixture()
def test_automation_setup():
	options = Options()
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')

	# To run headless
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')
	options.binary_location = '/usr/bin/google-chrome'
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
	return driver


def test_xss_found(test_automation_setup):
	xss_string = "<script>alert('javascript was executed')</script>"
	driver = test_automation_setup
	driver.get("http://172.25.0.1:5000/")
	driver.find_element("name","comment").send_keys(xss_string)
	driver.find_element("id","submit").click()
	try:
		WebDriverWait(driver, 5).until(expected_conditions.alert_is_present())

		alert = driver.switch_to.alert.accept()
		print("xss found")
		assert True
	
	except TimeoutException as ex:
		print("xss not found")
		assert False
	driver.close()