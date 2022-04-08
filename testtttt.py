from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs4
import requests as req
import time
import wget

driver_path = "/usr/bin/chromedriver"
driver = wd.Chrome(driver_path)

driver.get("chrome://downloads/")
