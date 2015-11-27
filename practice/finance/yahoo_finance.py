from mechanize import Browser
from BeautifulSoup import BeautifulSoup


url ="http://finance.yahoo.com/q/op?s=AAPL+Options"
# Mechanize --> Browser
br = Browser()
br.addheaders = [('User-agent','Firefox')]
br.set_handle_robots(False)
response = br.open(url)
content = response.read()

#BeautifulSoup --> BeautifulSoup

soup = BeautifulSoup(content)

#soup.findAll(text='AAPL151030C00070000')
##for y in soup.findAll('tr',{'data-row-quote':"_"}):
##    y.content
##
##    
## for y in soup.findAll('tr',{'data-row-quote':"_"}):
##	count = count + 1
##	if count <3 :
##		print y.td.text, y.td.next


for y in soup.findAll('tr',{'data-row-quote':"_"}):
	soup2 = BeautifulSoup(str(y))
	print ''
	for x in soup2.findAll('td'):
		print x.text,

		
