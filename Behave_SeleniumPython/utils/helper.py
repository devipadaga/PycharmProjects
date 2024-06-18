from configparser import ConfigParser
from selenium import webdriver
import os

def create_driver(browser):
  value = browser#os.environ.get('browser')
  if value == 'chrome':
    options=webdriver.ChromeOptions()
    driver = webdriver.Remote('http://localhost:8085',options=options)
#    driver=webdriver.chrome()
    driver.maximize_window()
    driver.implicitly_wait(time_to_wait=10)
    return driver
  elif value == 'firefox':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(time_to_wait=10)
    return driver