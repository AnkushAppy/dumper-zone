from mechanize import Browser
from BeautifulSoup import BeautifulSoup


#mechanize to get html file
br = Browser()
br.addheaders = [('User-agent','Firefox')]
br.set_handle_robots(False)

url = ["http://www.koimoi.com/category/reviews/",
	"http://www.bollywoodhungama.com/movies/reviews",
	"http://www.filmfare.com/reviews",
	"http://www.rediff.com/movies/reviews"]

url1 = "http://www.koimoi.com/category/reviews"	

response = br.open(url1)
#html file
content = response.read()

#BeautifulSoup
soup = BeautifulSoup(content)
links = soup.findAll('a',{'rel':'bookmark'})

#dictionary
d = {}
for link in links:
        if d.get(link.text,0) == 0:
                d[link.text] = link.get('href')

for name,linker in d:
        print name,linker
        
                





