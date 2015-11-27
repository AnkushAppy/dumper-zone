#-*- coding: utf-8 -*-
from mechanize import Browser
import requests
from BeautifulSoup import BeautifulSoup

url = "https://gru.inpi.gov.br/pePI/servlet/LoginController?action=login"

search_id = "PI0910270-1"
value_1 = {'submit':' Continuar » '}
response = requests.get(url,verify=False)
content = response.text

soup = BeautifulSoup(content)
input_t = soup('input')
for i in input_t:
    print i


##value = [('NumPedido','PI0910270-1'),('Submit',"botao")]
##res_ser = requests.get(url,data=value,verify=False)
##content = res_ser.text




