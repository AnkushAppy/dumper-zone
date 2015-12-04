from mechanize import Browser
from BeautifulSoup import BeautifulSoup
from goose import Goose
import time
from datetime import datetime

url = "http://www.thehindu.com"



br = Browser()
br.addheaders = [('User-agent','Firefox')]

count = 10
while count > 0:
	time.gmtime()
	count -= 1
	response = br.open(url)
	content = response.read()
	# till here article has been read....got html file
	# .....further we need to find today's important article's link
	# 
	#

	soup = BeautifulSoup(content)
	main_div = soup('div',{'class':'main-content mTop10'})
	soup2 = BeautifulSoup(str(main_div))
	links2 = soup2.findAll('a')
	d={};

	for lindex,link in enumerate(links2):
	    v = link.get('href').find('?')
	    st = link.get('href')[:v]
	    d[st] = lindex

	g = Goose()

	print datetime.now()

	for url_article in d:
	    article = g.extract(url = url_article)
	    print url_article
	    print '*-----*'*3
	    print article.title + ' : '
	    print article.meta_description

	time.sleep(300)

