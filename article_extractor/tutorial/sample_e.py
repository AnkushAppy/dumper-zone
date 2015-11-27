from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import requests
import os




search_url = "https://www.google.co.in/search?q='heavy'"
response = requests.get(search_url)
print response
soup = BeautifulSoup(response.text)
links = soup.findAll('h3',{'class':'r'})
print len(links)
for index,l in enumerate(links):
    article_url =  l.findChild().get('href')[7:l.findChild().get('href').find('&sa=')]
    article_text =  l.findChild()
    article_text_l = str(article_text)
    article_text_l =  article_text_l[article_text_l.find('>')+1:article_text_l.find('</a>')]
    print article_text_l.replace('<b>','').replace('</b>','')


##researchgate free ->  pdf
##def check_researchgate_for_pdf(url):
##    if url.find('researchgate') >=0 :
##        return True
##    return False

##article_url = 'http://www.researchgate.net/publication/237836402_Microstructural_evolution_and_mechanical_properties_of_dissimilar_Al-Cu_joints_produced_by_friction_stir_welding'
##article_response = requests.get(article_url)
##soup = BeautifulSoup(article_response.text)
##pdf_links = soup.findAll('a',{'class':'blue-link js-download rf btn btn-default'})
##pdf_src = str(pdf_links[0].get('href'))
##print check_researchgate_for_pdf(article_url),pdf_src


##date -> sciencedirect
##article_url = 'http://www.sciencedirect.com/science/article/pii/S0263224115003954'
##article_response = requests.get(article_url)
##soup = BeautifulSoup(article_response.text)
##date_upper_link = soup.findAll('dl',{'class':'articleDates'})
##date_link = str(date_upper_link[0].findChild().contents)
##print date_link
