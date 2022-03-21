# Author: Tracy Vierra
# Date Created: 3/21/2022
# Date Modified: 3/21/2022

# Description:

# Usage:

from termios import B1000000
import openpyxl
import os

os.chdir('C:\\Users\\tracy\Documents\\Python Scripts\\git\\vigilant-pancake\\ATBS')

workbook = openpyxl.load_workbook('example.xlsx')
sheet = workbook.get_sheet_by_name('Sheet1')
# type(sheet)

# class 'openpyxl.worksheet.worksheet.Worksheet'
workbook.get_sheet_names()

cell = sheet['A1']
cell.value
print(str(cell.value))
print(str(sheet['A1'].value))	# if you don't want to save the cell 
print(str(sheet['B1'].value))		
print(str(sheet['C1'].value))


