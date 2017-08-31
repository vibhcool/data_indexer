import PyPDF2
import requests
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

stemer = SnowballStemmer("english")


data = {}

pdf_file = open('Jul_2013_SOLE SANJAY SHRIVANT.pdf', 'rb')

pdf = PyPDF2.PdfFileReader(pdf_file)
page_count = pdf.getNumPages()
print(page_count)
for page_no in range(0, page_count):
    pageObj = pdf.getPage(page_no)
    data[page_no] = pageObj.extractText()
    # print(pageObj.extractText())
# print(data)

stop = set(stopwords.words("english"))

for num, value in data.items():
    word = nltk.word_tokenize(value)
    tag_word = nltk.tag.pos_tag(word)
    token = [t.lower() for t, tag in tag_word if t not in stop if tag == 'NNP']
    print(token)
    wordfreq = nltk.FreqDist(token)
    #print(wordfreq.most_common(10))
    imp = wordfreq.most_common(10)





