from mechanize import Browser
from BeautifulSoup import BeautifulSoup

br = Browser()
br.addheaders = [('User-agent','Firefox')]
br.set_handle_robots(False)


login_url = "https://www.strava.com/login"
login_page = br.open(login_url)

print br.response()

br.form = list(br.forms())[0] 
br['email'] = 'email@email.com'
br['password'] = 'password'

new_response = br.submit()
print "Kitten Kitten"

