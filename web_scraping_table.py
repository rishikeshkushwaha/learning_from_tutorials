import urllib2
from urllib2 import Request
from bs4 import BeautifulSoup


#A small tutorial to read a table and then scarpe data into table format

def make_soup(url):
    theurl = Request(url)
    thepage = urllib2.urlopen(theurl)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

#soup = make_soup("http://www.basketball-reference.com/players/a/")
soup = make_soup("http://erail.in/?T=HPT::YPR")

for record in soup.findAll('td'):
    for data in record.findAll('td'):
        for info in data.findAll('a'):
            print info.text

for r in soup.findAll('div', {"class":"BackColor2"}):
        print r.find('a').text
