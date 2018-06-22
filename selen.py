
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import configparser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import bs4
#from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re


browser = webdriver.Chrome()




config = configparser.ConfigParser()
config.read('souperssl.cfg')

user = config['login']['user']
passwd = config['login']['passwd']
myurl = config['login']['myurl']

browser.get(myurl)

element_user = browser.find_element_by_name("SWEUserName")
element_pass = browser.find_element_by_name("SWEPassword")
element_send = browser.find_element_by_id("s_swepi_22")


element_user.send_keys(user)
element_pass.send_keys(passwd)
element_send.click()


#element_Kunden = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'Kunden')))

#wait = WebDriverWait(browser, 30)
#element_kunden = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Kunden')))

time.sleep(13)

browser.find_element_by_link_text("Kunden").click()
time.sleep(1)
browser.find_element_by_id("s_2_1_42_0_Ctrl").click()
time.sleep(1)

#data = []
#for tr in browser.find_element_by_id('s_1_l'):
#    tds = tr.find_element_by_id('td')
#    if tds: 
#        data.append([td.text for td in tds])
#print(data)

soup_level1=soup(browser.page_source, 'lxml')
print (browser.page_source)
#table = soup_level1.find_all('table')[0]

#print(table)

#browser.quit()