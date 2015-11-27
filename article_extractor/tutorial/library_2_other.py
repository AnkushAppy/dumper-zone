from mechanize import Browser
from BeautifulSoup import BeautifulSoup

import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import time
import xlsxwriter


lookup_table = 'Library1.xlsx'
book_vl = xlrd.open_workbook(lookup_table)
sheet_vl = book_vl.sheet_by_index(0)

temp_book = xlsxwriter.Workbook('final_url.xlsx')
temp_worksheet = temp_book.add_worksheet()


br = Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
br.addheaders = [('User-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:41.0) Gecko/20100101 Firefox/41.0')]

for x in range(sheet_vl.nrows):
    val_url = sheet_vl.cell_value(rowx = x,colx = 6)
    val_title = sheet_vl.cell_value(rowx = x,colx = 1)
    val_title = val_title + '.pdf'
    response = br.open(val_url)
    soup = BeautifulSoup(response.read())
    #pdf_title
    # for col in range(sheet_vl.ncols):
    #     temp_worksheet.write(x,col,sheet_vl.cell_value(rowx = x,colx = col))
    links = soup.findAll('iframe')
    for l in links:
        print l.get('src')
        #temp_worksheet.write(x,1,l.get('src'))
        resp_pdf = br.open(str(l.get('src')))
        f = open('pdf/%s'%(val_title),'w')
        f.write(resp_pdf.read())
        f.close()
        

temp_book.close()