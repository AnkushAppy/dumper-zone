import requests
from BeautifulSoup import BeautifulSoup
from mechanize import Browser
from lxml import html
from lxml.html import parse, submit_form
 
temp_mail_url = 'http://temp-mail.org/en/'
twitter_url = 'https://twitter.com/signup'

def email_id_fetcher():  ##fetching temp_mail_url, get email 
    response = requests.get(temp_mail_url)
    soup = BeautifulSoup(response.text)
    links = soup.findAll('input',{'id':'mail'})
    temp_mail_id = links[0].get('value')
    return temp_mail_id

#def account_creator():    
E_MAIL = email_id_fetcher()

resp_signup = requests.get(twitter_url)
tree= html.fromstring(resp_signup.text)

#form submission
links_forms = tree.forms[3]
links_forms.fields['user[name]'] = 'tony.blair.righthand1'
links_forms.fields['user[user_password]'] = 'Great_wall_2'
links_forms.fields['user[email]'] = E_MAIL
new_response = requests.get(submit_form(tree.forms[3]))
##links_forms.fields = {
##    'user[name]':'tony.blair.righthand1',
##    'user[user_password]':'Great_wall_2',
##    'user[email]' : bytes(E_MAIL),
####    'authenticity_token' : tree.forms[3].fields['authenticity_token']
##    }
new_response = requests.get(submit_form(tree.forms[3]))






