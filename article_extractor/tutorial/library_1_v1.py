from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import requests
import os

import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import time
import xlsxwriter


baseurl = "https://www.google.co.in/search?q="
lookup_table = 'Articles.xlsx'
book_vl = xlrd.open_workbook(lookup_table)
sheet_vl = book_vl.sheet_by_index(0)


br = Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
br.addheaders = [('User-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:41.0) Gecko/20100101 Firefox/41.0')]
count = 0
for x in range(sheet_vl.nrows):
    count = count + 1
    if count < 21:
        continue
    val_sno = sheet_vl.cell_value(rowx = x,colx = 0)
    print val_sno
    val_title = sheet_vl.cell_value(rowx = x,colx = 1)
    final_title = str(val_sno) + str(val_title)
    #val_title = val_title + '.pdf'
    search_url = str(baseurl) + '"' + str(val_title) + '"'
    #response = br.open(str(search_url))  #google search
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text)
    
    #links = soup.findAll('cite',{'class':'_Rm'})
    links = soup.findAll('cite')
    #for l in links:  # correction needed
    
    referal_url = str(links[0].text)
    index_of_slash = referal_url.find('/')
    new_referal_url = referal_url[:index_of_slash] + ".sci-hub.org" + referal_url[index_of_slash:]
    new_referal_url = 'http://' + new_referal_url

    #temp_worksheet.write(x,1,l.get('src'))
    try:
        resp_pdf = br.open(new_referal_url)  # ieee/sciencedirectl link found
        soup = BeautifulSoup(resp_pdf.read())
        #pdf_title
        # for col in range(sheet_vl.ncols):
        #     temp_worksheet.write(x,col,sheet_vl.cell_value(rowx = x,colx = col))
        links = soup.findAll('iframe')
        
        for l in links:
            print l.get('src')
    #         #temp_worksheet.write(x,1,l.get('src'))
    #         resp_pdf = br.open(str(l.get('src')))
    #         path_ev = os.getcwd()
    #         path_ev = path_ev + '/pdf/' + str(val_sno) +'.pdf'
    #         f = open(path_ev,'w')
    #         f.write(resp_pdf.read())
    #         f.close()
    # except:
    #     pass
