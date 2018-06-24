
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
import pandas as pd
import sys
import csv


browser = webdriver.Chrome()




config = configparser.ConfigParser()
config.read('souperssl.cfg')


'''

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



time.sleep(20)




browser.find_element_by_link_text("Kunden").click()
time.sleep(2)
#suchen
browser.find_element_by_id("s_2_1_42_0_Ctrl").click()
time.sleep(2)
#show more results
browser.find_element_by_id("s_1_1_4_0_mb").click()
time.sleep(2)
'''


#get html source
#data = open("page.html")
#data.read()
#print(data)
#soup_level1=soup(data, 'lxml')

browser.get("file:///home/rox/github/souper/page.html")

soup_level1=soup(browser.page_source,"lxml")
#print (soup_level1)
#table = soup.findAll('table', attrs={ "id" : "s_1_l"})
#table = soup_level1.select('#s_1_l')
tables = soup_level1.find('table',id="s_1_l")




csvout  = csv.writer(sys.stdout)

for table in tables:
    print ('#')
    print ('# Table')
    print ('# Fields: ' + ','.join([tr.text for tr in table.findAll('th')]))
    
    for row in table.findAll('tr'):
        csvout.writerow([tr.text for tr in row.findAll('td')])
    print


'''

headers = [header.text for header in table.find_all('th')]
#print(header)

headers = [header.text for header in table.find_all('th')]
print(headers)

rows = []
for row in table.find_all('tr'):

    rows.append([val.text.encode('utf8') for val in row.find_all('td')])


with open('output_file.csv', 'wb') as f:
    
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerow(row for row in rows if row)
'''


#next


'''
for a in range (45):
    browser.find_element_by_id("last_pager_s_1_l").click()
    #WebDriverWait(browser,10,poll_frequency=0.5).until(EC.element_to_be_clickable((By.ID, 'last_pager_s_1_l'))).click()
    time.sleep(2)
'''
            



'''
data = []
for tr in browser.find_element_by_id('s_1_l'):
    tds = tr.find_element_by_id('td')
    if tds: 
        data.append([td.text for td in tds])
print(data)
'''

#print (browser.page_source)
#table = soup_level1.find_all('table')[0]

#print(table)





browser.quit()