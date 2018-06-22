import configparser
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import wget
import ssl





config = configparser.ConfigParser()
#config.sections()
config.read('souperssl.cfg')

#print (config.sections())
#print(config['login']['user'])
#print(config['login']['passwd'])
user = config['login']['user']
passwd = config['login']['passwd']
myurl = config['login']['myurl']


print(myurl + " " + user + " " + passwd)

ssl._create_default_https_context = ssl._create_unverified_context
wget.download(myurl)

uClient = uReq(myurl)
#page_html = uClient.read()
page = uClient.get(myurl, auth=(user,passwd), verify=False)
#page_html = uClient.read()
#print(page_html)

uClient.close()
