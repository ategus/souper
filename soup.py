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


container_count = len(containers)

contain = containers[0]

filename = "products.csv"
f = open(filename,"w")

headers = "name; price\n"

f.write(headers)



for c in range (0,container_count):
    res = containers[c].find_all("div",{"class":"price orange"})
    res2 = re.split('\s+', str(res))
    if len(res2)>1:
        price = res2[6]
    description = containers[c].find_all("img",{"class":"lazyload"})
    for imgage in description:
        des = imgage['alt']
    print(des + "  " + price + "€")
    f.write(des + ";" + price + "\n")

f.close
