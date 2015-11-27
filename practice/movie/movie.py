from mechanize import Browser
from BeautifulSoup import BeautifulSoup

url = "http://www.imdb.com/trailers?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2253984442&pf_rd_r=1QNFVJ4BCR6JDJ6830A3&pf_rd_s=hero&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_hp_sm&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2253984442&pf_rd_r=1QNFVJ4BCR6JDJ6830A3&pf_rd_s=hero&pf_rd_t=15061&pf_rd_i=homepage"

br = Browser()
br.set_handle_robots(False)
br.addheades = [('User-agent','Firefox')]
response = br.open(url)
content = response.read()
#BeautifulSoup

soup = BeautifulSoup(content)
links  = soup.findAll('div',{'class':'trailer-caption'})
for x in links:
	print x.text

