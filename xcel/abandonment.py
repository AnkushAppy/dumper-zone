# Read but writes in new copied file
# Change input file_name

import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
#file_path = 'C:/Users/Dolcera/Desktop/script/f2.xlsx'
file_path = 'demo_1.xlsx'
book = xlrd.open_workbook(file_path)
sh = book.sheet_by_index(0)
wb = copy(book)
ws = wb.get_sheet(0)
count = 0
for rx in range(sh.nrows):
    legal_status = sh.cell_value(rowx=rx,colx=16)
    first_split = legal_status.split('|')[0]
    print first_split
    if first_split.find("EXPIRED") != -1:
        ws.write(rx,26,"Abandon")
        count = count +1
    elif first_split.find("LAPS") != -1:
        ws.write(rx,26,"Abandon")
        count = count +1
    elif first_split.find("LAPSE") != -1:
        ws.write(rx,26,"Abandon")
        count = count +1
    elif first_split.find("ABANDON") != -1:
        ws.write(rx,26,"Abandon")
        count = count +1
    elif first_split.find("FAILURE") != -1:
        ws.write(rx,26,"Abandon")
        count = count +1
    elif first_split.find("CEASE") != -1:
        ws.write(rx,26,"Abandon")
        count = count +1
    elif first_split.find("CEASED") != -1:
        ws.write(rx,26,"Abandon")
        count = count +1
    elif first_split.find("EXPIRY") != -1:
        ws.write(rx,26,"Abandon")
        count = count +1
    elif first_split.find("WITHDRAWN") != -1:
        ws.write(rx,26,"Abandon")
        count = count +1
    elif first_split.find("DEAD") != -1:
        ws.write(rx,26,"Abandon")
        count = count +1
    else:
        ws.write(rx,26,"Fine")
wb.save('demo_example.xls')
print count
