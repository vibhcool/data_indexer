import PyPDF2
import requests

data = {}

url = input('Enter pdf file link: ')
if len(url) > 5:
    url = ''
    r=requests.get(url)
else:
    pdf_file = open('Jul_2013_SOLE SANJAY SHRIVANT.pdf', 'rb')

pdf = PyPDF2.PdfFileReader(pdf_file)
page_count = pdf.getNumPages()
print(page_count)
for page_no in range(0, page_count):
    pageObj = pdf.getPage(page_no)
    data[page_no] = pageObj.extractText()
    #print(pageObj.extractText())
print(data)
