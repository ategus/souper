import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

myurl = 'https://www.cyberport.de/gaming/gaming-monitore.html'

uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")

#grab container
containers = page_soup.find_all("div",{"class":"productWrapper"})
#containers = page_soup.find_all("article")

container_count = len(containers)

contain = containers[0]
price = contain.find_all("div",{"class":"price orange"})
#price = contain.find_all("span")

price

result = re.split('\s+', str(price))


print (result[6])
#print(containers)
#print(contain)

#print (container_count)

#logging.info(contain)
#print (containers[0]    )
#print(result)