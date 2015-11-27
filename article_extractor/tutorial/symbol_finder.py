import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import time
import xlsxwriter

def symbol_coverter(val_title):
    str_url = ''
    for x in val_title:
    	if x.isspace():
    		str_url = str_url + x
    	if x.isalnum():
    		str_url = str_url + x
    return str_url