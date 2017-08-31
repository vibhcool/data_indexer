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
imp = {}
token=[]
for num, value in data.items():
    word = nltk.word_tokenize(value)
    tag_word = nltk.tag.pos_tag(word)
    token.append([t.lower() for t, tag in tag_word if t not in stop if tag == 'NNP'])
    #print(token[num])
    wordfreq = nltk.FreqDist(token[num])
    #print(wordfreq.most_common(10))
    imp[num+1] = [t for t,key in wordfreq.most_common(10)]

req={}
for key, value in imp.items():
    for word in value:
        if word in req:
            continue
        a=[key]
        req[word]=a
        for i in range(key,page_count):
            if word in token[i]:
                req[word].append(i+1)

for word, num in req.items():
    print(word+" : ", end=' ')
    for i in num:
        print(i,end=' ')
    print()





