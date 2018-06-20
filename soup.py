import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myurl = 'https://www.cyberport.de/gaming/gaming-monitore.html'

uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
#print(page_soup.body.span

result = page_soup.find_all("div",{"class":"productWrapper"})

print(result)