import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import time
import xlsxwriter

start_time = time.time()
lookup_table = 'test_1.xlsx'
data_table = 'test_1_copy.xlsx'
book_vl = xlrd.open_workbook(lookup_table)
book_dt = xlrd.open_workbook(data_table)
sheet_vl = book_vl.sheet_by_index(0)
sheet_dt = book_dt.sheet_by_index(0)
temp_book = xlsxwriter.Workbook('example.xlsx')
temp_worksheet = temp_book.add_worksheet()

vlk_inp_1 = int(raw_input("1st vlookup input "))
vlk_inp_2 = int(raw_input("2nd vlookup input "))
vlk_inp_3 = int(raw_input("3rd vlookup input "))
vlk_inp_4 = int(raw_input("4th vlookup input column to be modified "))

dictionary_for_data_table = {}

for y in range (sheet_dt.nrows):
    dictionary_for_data_table[sheet_dt.cell_value( rowx = y, colx = vlk_inp_2)] = sheet_dt.cell_value( rowx = y, colx = vlk_inp_3)

for x in range(sheet_vl.nrows):
    val = sheet_vl.cell_value(rowx = x,colx = vlk_inp_1)
    for col in range(sheet_vl.ncols):
        temp_worksheet.write(x,col,sheet_vl.cell_value(rowx = x,colx = col))
    temp_worksheet.write(x,vlk_inp_4,dictionary_for_data_table.get(val))  
temp_book.close()
end_time = time.time()
print end_time - start_time
