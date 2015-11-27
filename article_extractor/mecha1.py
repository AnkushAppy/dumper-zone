import mechanize
#creating browser
from BeautifulSoup import BeautifulSoup 

br = mechanize.Browser()
#br.set_all_readonly(False)
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent','Firefox')]

#opening webpage

url = 'http://www.google.com'
respone = br.open(url)

# finding form
for forms in br.forms():
    print "Form name: ",forms.name
    print forms


# select form
br.select_form("f")

# submitting form
br['q'] = "Facebook"
br.method = "POST"
response = br.submit()
content  = response.read()

#print content
#print content

#soup
soup = BeautifulSoup(content)
#links collection

links = soup.findAll('a',{'onmousedown'})
print links

##file_op = open("foo.txt",'wb')
##for l in links:
##   file_op.write(str(l.get('href')))
   
for i in links:
    str = ''
	for x in i:
            









