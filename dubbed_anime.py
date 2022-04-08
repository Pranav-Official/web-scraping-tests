from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs4
import requests as req
import time
import wget


url = "https://ww5.dubbedanime.net/anime/3539-golden-kamuy"
data = req.get(url)
data = data.text
soup = bs4(data,'html.parser')
div = soup.find_all("div",{"class":"da-video-tbl"})
eps = []

for ele in div:
    eps.append("https://ww5.dubbedanime.net" + ele.a['href'] + "-english-sub")
    
eps.sort()
print(eps)

driver_path = "/usr/bin/chromedriver"
driver = wd.Chrome(driver_path)

driver.get(eps[0])

time.sleep(2)
try:
    driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li[7]/a").click()
except:
    driver.find_element_by_xpath("/html/body/nav/div/div[1]/button").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li[7]/a").click()
    

usename_filed = driver.find_element_by_id("login-username")
password_filed = driver.find_element_by_id("login-password")

usename_filed.send_keys("KakashiHatake")
password_filed.send_keys("Z3#!wvSwkS8rkd$")


login_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button")
login_button.click()

time.sleep(5)
button = driver.find_element_by_id("download-video")

button.click()




