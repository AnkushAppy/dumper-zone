from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import requests
import os
import urllib

import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import time
import xlsxwriter
import xlwt

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

def check_researchgate_for_pdf(url):
    if url.find('researchgate') >=0 :
        return True
    return False
def check_sciencedirect_link(url):
    if url.find('sciencedirect') >=0 :
        return True
    return False
    

baseurl = "https://www.google.co.in/search?q="
lookup_table = 'Articles2.xlsx'
book_vl = xlrd.open_workbook(lookup_table)
sheet_vl = book_vl.sheet_by_index(0)

wb = xlwt.Workbook()
ws = wb.add_sheet('sheet1')
ws.write(0,0,'val_sno')
ws.write(0,1,'title')
ws.write(0,2,'link')
ws.write(0,3,'date')


fp = open('links.txt','w')
fp_error = open('errors.txt','w')
br = Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
br.addheaders = [('User-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:41.0) Gecko/20100101 Firefox/41.0')]
for x in range(sheet_vl.nrows):
    val_sno = sheet_vl.cell_value(rowx = x,colx = 0)
    val_title = sheet_vl.cell_value(rowx = x,colx = 1)
    print '*'*50
    print int(val_sno), val_title
    search_url = str(baseurl) + val_title[:50]
    pdf_link_found = False
    pdf_link_is = 'Not Found'
    article_url_is = 'Not Found'
    date_found_is = 'Not Found'
    title1 = symbol_converter(val_title)
    try:

        response = requests.get(search_url)
        #print "Google search done..."
        soup = BeautifulSoup(response.text)
        links = soup.findAll('h3',{'class':'r'})
        #print links
        for index,l in enumerate(links):
            #print index
            article_url =  l.findChild().get('href')[7:l.findChild().get('href').find('&sa=')]
            article_text =  l.findChild()
            article_text_l = str(article_text)
            article_text_l =  article_text_l[article_text_l.find('>')+1:article_text_l.find('</a>')]
            title2 = symbol_converter(article_text_l.replace('<b>','').replace('</b>',''))
            
            #print title1[:30]
            #print title2[:30]
            if text_compare(title1[:20],title2[:20]):
                article_url_is = article_url
                try:
                    if article_url.find('.pdf') != -1:
                        #print "link found on google itslef...." + article_url
                        fp.write('%d %s'%(val_sno,article_url))
                        pdf_link_found = True
                        pdf_link_is = article_url
                        continue
                    elif check_researchgate_for_pdf(article_url):
                        #print 'entered'
                        article_response = requests.get(article_url)
                        soup = BeautifulSoup(article_response.text)
                        pdf_links = soup.findAll('a',{'class':'blue-link js-download rf btn btn-default'})
                        pdf_src = str(pdf_links[0].get('href'))
                        pdf_link_found = True
                        pdf_link_is = pdf_src
                        #print "researchgate pdf link..." + pdf_src

                    if pdf_link_found == False:
                        index = sci_hub(article_url)
                        sci_hub_url = str(article_url[:index] + ".sci-hub.org" + article_url[index:])
                        article_response = requests.get(sci_hub_url)
                        soup = BeautifulSoup(article_response.text)
                        pdf_links = soup.findAll('iframe')
                        pdf_iframe = str(pdf_links[0].get('src'))
                        pdf_link_found = True
                        pdf_link_is = pdf_iframe
                        #print "Sci-hub links" + pdf_iframe
                        fp.write('%d %s'%(val_sno,pdf_iframe))


                        
                    if check_sciencedirect_link(article_url):
                        article_response = requests.get(article_url)
                        soup = BeautifulSoup(article_response.text)
                        date_upper_link = soup.findAll('dl',{'class':'articleDates'})
                        date_link = str(date_upper_link[0].findChild().contents)
                        date_final = date_link[7 + date_link.find('online'):-2]
                        date_found_is = date_final
                        #print 'sciencedirect date...' + date_final
                        

                except Exception as e:
                    #print "No sci-hub/ or some other error" + article_url
                    #print e.message
                    pass
                    
        
    except Exception as e:
        #print e.message
        pass

    ws.write(x+1,0,val_sno)
    ws.write(x+1,1,title1)
    
    ws.write(x+1,3,date_found_is)

    if pdf_link_found == True:
        print pdf_link_is
        print date_found_is
        
        title1 = str(val_sno) + str(title1) + '.pdf'
        try:
            urllib.urlretrieve(pdf_link_is,title1)
        except:
            print "can't download pdf"
            pass
    else:
        print article_url_is
        ws.write(x+1,2,article_url_is)
        print date_found_is

    wb.save('article_finder.xls')
