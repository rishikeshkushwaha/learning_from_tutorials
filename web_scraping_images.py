import urllib2
from urllib2 import Request
from bs4 import BeautifulSoup
import os

#simple tutorial to scape images from site

def make_soup(url):
    theurl = Request(url)
    thepage = urllib2.urlopen(theurl)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata


soup = make_soup("https://uwaterloo.ca")
for img in soup.findAll('img'):
    temp =img.get('src')
    if temp[:1]=="/":
        image = "https://uwaterloo.ca"+temp
    else:
        image = temp
    print(img.get('src'))

    i = 1
    nametemp = img.get('alt')
    if len(nametemp) == 0:
        filename =str(i)
        i = i+1
    else:
        filename= nametemp

    imagefile = open(filename + ".jpeg",'wb')
    theimage = Request(image)
    imagefile.write(urllib2.urlopen(theimage).read())
    imagefile.close()
