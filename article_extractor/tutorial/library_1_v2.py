from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import requests
import os

import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import time
import xlsxwriter

def symbol_converter(val_title):
    str_url = ''
    for x in val_title:
        try:
            x.decode('ascii')
            if x.isspace():
                str_url = str_url + x
            if x.isalpha():
                str_url = str_url + x
            if x.isdigit():
                str_url = str_url + x
        except:
            pass
    return str_url

def sci_hub(sci_hub_url):
    #find third '/' :P
    count = 0
    for index,x in enumerate(sci_hub_url):
        if x =='/':
            count = count + 1 
        if count == 3:
            return index
def text_compare(str1,str2):
    if str1.lower() == str2.lower():
        return True
    return False

    

baseurl = "https://www.google.co.in/search?q="
lookup_table = 'Articles2.xlsx'
book_vl = xlrd.open_workbook(lookup_table)
sheet_vl = book_vl.sheet_by_index(0)


fp = open('links.txt','w')
fp_error = open('errors.txt','w')
br = Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
br.addheaders = [('User-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:41.0) Gecko/20100101 Firefox/41.0')]
for x in range(sheet_vl.nrows):
    val_sno = sheet_vl.cell_value(rowx = x,colx = 0)
    val_title = sheet_vl.cell_value(rowx = x,colx = 1)
    #spaced_val_title = val_title.replace(' ','+')
    print '*'*50
    print int(val_sno), val_title
    search_url = str(baseurl) + val_title
    try:

        response = requests.get(search_url)
        print "Google search done..."
        soup = BeautifulSoup(response.text)
        
                
        #links = soup.findAll('cite',{'class':'_Rm'})
        links = soup.findAll('h3',{'class':'r'})
        article_url = links[0].findChild().get('href')[7:links[0].findChild().get('href').find('&sa=')]
        #print links[0].findChild().get('href').contents
        if article_url.find('.pdf') != -1:
            print "link found on google itslef...." + article_url
            fp.write('%d %s'%(val_sno,article_url))
            continue
        index = sci_hub(article_url)
        sci_hub_url = str(article_url[:index] + ".sci-hub.org" + article_url[index:])
        article_response = requests.get(sci_hub_url)
        soup = BeautifulSoup(article_response.text)
        pdf_links = soup.findAll('iframe')
        pdf_iframe = str(pdf_links[0].get('src'))
        print "Sci-hub links" + pdf_iframe
        fp.write('%d %s'%(val_sno,pdf_iframe))
        # pdf_response = requests.get(pdf_iframe)

        # val_title = symbol_converter(val_title)
        # pdf_title = str(int(val_sno)) + ' ' + val_title + '.pdf'
        # fp = open('./pdf2/%s'%pdf_title,'w')
        # fp.write(pdf_response.text)
        # fp.close() 
    except Exception as e:
        print "except occurred - > %s"%article_url, e.message
        fp_error.write('%d %s %s \n'%(val_sno,val_title, e.message))
        fp_error.write('####'*6)
        pass

fp.close()
print "Completed!"
