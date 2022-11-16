from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
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


def test_login_success(test_automation_setup):
	driver = test_automation_setup
	driver.get("http://172.25.0.1:5000/")
    