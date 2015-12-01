import xlrd
from xlrd import open_workbook
import time
import xlsxwriter
import string

def abc_generator():
	return string.ascii_uppercase

def last_column_name_in_alpha(col_length):
	column_name = abc_generator()
	return 'B:' + column_name[col_length/26] + column_name[col_length%26]




#opening file to read
data_table = 'test_small.xlsx'
book_opened_in_xlrd = xlrd.open_workbook(data_table)
sheet_opened_in_xlrd = book_opened_in_xlrd.sheet_by_index(0)

row_length = sheet_opened_in_xlrd.nrows
col_length = sheet_opened_in_xlrd.ncols


#opening file to write
temp_book = xlsxwriter.Workbook('example.xlsx')
worksheet = temp_book.add_worksheet()


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

#format_for_sno.set_font_color('red')
#						'border':5,'font_name':'calibri','font_color':'white',})

#						'bg_color':'blue','align':'center',})
# bold = workbook.add_format({'bold': True})
#different formats
#for y in range (sheet_opened_in_xlrd.nrows):

for y in range(row_length+1):
	worksheet.set_row(y,30)
#for x in range(1,col_length+1):

worksheet.set_column(last_column_name_in_alpha(col_length), 30)
worksheet.set_column('A:A', 10)
##worksheet.set_column(0, 20)
worksheet.freeze_panes(1, 0) # parameters are (first row, how many row)


format_for_sno, format_for_first_column, simple_format = sheet_formats()

worksheet.write(0,0,'S.No.',format_for_sno)
for y in range(row_length-1):
	worksheet.write(y+1,0,y+1,format_for_sno)

for x in range(col_length):
	worksheet.write(0,x+1,sheet_opened_in_xlrd.cell_value(0,x),format_for_first_column)

for x in range(1,row_length):
	print sheet_opened_in_xlrd.row_types(x,0)
	for y in range(col_length):
		value = sheet_opened_in_xlrd.cell_value(x,y)
		#print value
		if value == 42 and (sheet_opened_in_xlrd.row_types(x,y,y+1)[0] == 5) :
			print 'lol'
			worksheet.write_blank(x,y+1,'',simple_format)
		else:
			worksheet.write(x,y+1,value,simple_format)


temp_book.close()

