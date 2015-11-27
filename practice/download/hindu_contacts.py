from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import re

url = "http://www.thehindu.com/navigation/?type=static&page=contact"

br = Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','Firefox')]
response = br.open(url)
content = response.read()

soup = BeautifulSoup(content)

#iframe

src = soup.iframe['src']

response = br.open(src)
content = response.read()

soup = BeautifulSoup(content)

mails = soup.findAll('a')

d ={}

for i,e in enumerate(mails):
        st = e.get('href')
        if d.get(st,0) == 0:
                d[st] = i
                print st[7:]

		
	
