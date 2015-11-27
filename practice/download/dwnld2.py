# using mechanize and BeautifulSoup

from mechanize import Browser
from BeautifulSoup import BeautifulSoup

br = Browser()
br.addheaders = [('User-agent','Firefox')]
br.set_handle_robots(False)
response = br.open("http://imgur.com/")
content =  response.read()


# BeautifulSoup
soup = BeautifulSoup(content)

images = soup.findAll('img')

for image in images[0:10]:
	src = image.get('src')
	resp = br.open(src)
	print src
	f = open('download_image1/%s'% src.split('/')[-1],'w')
	f.write(resp.read())
	f.close()
