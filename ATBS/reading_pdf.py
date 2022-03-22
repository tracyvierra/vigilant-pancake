# Author: Tracy Vierra
# Date Created: 3/21/2022
# Date Modified: 3/21/2022

# Description:

# Usage:

import PyPDF2
import os

os.chdir('C:\\Users\\tracy\\Documents\\Python Scripts\\git\\vigilant-pancake\\ATBS')

pdfFile = open('meetingminutes1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

pdfReader.numPages

page= pdfReader.getPage(0)
page.extractText()

for pageNum in range(pdfReader.numPages):
    print(pdfReader.getPage(pageNum).extractText())

