# Read but writes in new copied file
# Change input file_name
#
#
# Change at multiple places
#

import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
#file_path = 'C:/Users/Dolcera/Desktop/script/f2.xlsx'
file_path = 'oil_2005_2.xlsx'
book = xlrd.open_workbook(file_path)
sh = book.sheet_by_index(0)
wb = copy(book)
ws = wb.get_sheet(0)
for rx in range(sh.nrows):
    prority_country = sh.cell_value(rowx=rx,colx=4)
    if prority_country.find("WO") != -1:
        ws.write(rx,16,"PCT")
    else:
        ws.write(rx,16,"NO")
wb.save('demo_example.xls')
