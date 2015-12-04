import xlrd
from xlrd import open_workbook
import time
import xlsxwriter
import string

def abc_generator():  
	# str = [ABCD.....Z]
	return string.ascii_uppercase

def last_column_name_in_alpha(col_length):
	#column name A,B,Z.........AA,AB,AC........AZ,BA.....ZZ
	#to get name of last column in alphabet format
	column_name = abc_generator()
	return 'B:' + column_name[col_length/26] + column_name[col_length%26]

def sheet_formats():
	format_for_sno = temp_book.add_format({'bold': True ,'font_color':'white','font_name':'calibri','font_size':11,'align':'center','bg_color':'#4F81BD'})
	format_for_sno.set_border(1)
	format_for_sno.set_text_wrap()
	format_for_sno.set_align('top')
	format_for_first_column = temp_book.add_format({'bold': True ,'font_color':'white','font_name':'calibri','font_size':11,'align':'center','bg_color':'#4F81BD'})
	format_for_first_column.set_border(1)
	format_for_first_column.set_text_wrap()
	format_for_first_column.set_align('top')
	simple_format = temp_book.add_format({'font_name':'calibri','font_size':11})
	simple_format.set_border(1)
	simple_format.set_text_wrap()
	simple_format.set_align('left')
	simple_format.set_align('top')
	return format_for_sno, format_for_first_column, simple_format

def date_finder(date_string):
	# if date then return true else false
	# code yet to be written.......
	return True


#opening file to read
data_table = 'test_small.xlsx'
book_opened_in_xlrd = xlrd.open_workbook(data_table)
sheet_opened_in_xlrd = book_opened_in_xlrd.sheet_by_index(0)
row_length = sheet_opened_in_xlrd.nrows
col_length = sheet_opened_in_xlrd.ncols
#opening new file to write
# we can't write on existing file thats why we need to create another file and copy content of file we just read. 
temp_book = xlsxwriter.Workbook('example.xlsx')
worksheet = temp_book.add_worksheet()
#setting row height, applicable on worksheet
for y in range(row_length+1):
	worksheet.set_row(y,30)
#setting column width, applicable on worksheet
worksheet.set_column(last_column_name_in_alpha(col_length), 30)
worksheet.set_column('A:A', 10)
# parameters are (first row, how many row) : freeze pane
worksheet.freeze_panes(1, 0)
#collecting different formats.....function sheet_format() is called
format_for_sno, format_for_first_column, simple_format = sheet_formats()

#s.no. at 0,0 # numbering at 0th column 
worksheet.write(0,0,'S.No.',format_for_sno)
for y in range(row_length-1):
	worksheet.write(y+1,0,y+1,format_for_sno)

#copyinh headings
for x in range(col_length):
	worksheet.write(0,x+1,sheet_opened_in_xlrd.cell_value(0,x),format_for_first_column)

#copying others
for x in range(1,row_length):
	for y in range(col_length):
		value = sheet_opened_in_xlrd.cell_value(x,y)
		if value == 42 and (sheet_opened_in_xlrd.row_types(x,y,y+1)[0] == 5) :
			worksheet.write_blank(x,y+1,'',simple_format)
		else:
			worksheet.write(x,y+1,value,simple_format)


temp_book.close()

