import requests
from BeautifulSoup import BeautifulSoup
c =requests.Session()
url = "http://www.noobmovies.com/accounts/login/?next=/"
headers_1 = {'User-Agent': 'Mozilla/5.0'}
payload_1 = {'username':'my_username','password':'my_password'}

#payload = dict(username=Username,password=Password,next='/')
page = c.get(url)

soup = BeautifulSoup(page.text)
print soup.findAll('input')
    
    



