import urllib2
from urllib2 import Request
from bs4 import BeautifulSoup
import os

#A small tutorial to read a table and then scarpe data into table format
#and create .csv file to save it also.

def make_soup(url):
    theurl = Request(url)
    thepage = urllib2.urlopen(theurl)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = make_soup("http://www.basketball-reference.com/players/a/")
#soup = make_soup("http://erail.in/?T=HPT::YPR")


playerdatasaved =""
for record in soup.findAll('tr'):
    playerdata=""
    for data in record.findAll('td'):
        playerdata = playerdata+","+data.text
    playerdatasaved = playerdatasaved +"\n" + playerdata[1:]

print playerdatasaved
headed ="From,To,Pos,Ht,Wt,Birth Date,Birth Year,College"+"\n"
file1 = open(os.path.expanduser("basketball.csv"),"wb")
file1.write(bytes(headed))
file1.write(bytes(playerdatasaved))
##for r in soup.findAll('div', {"class":"BackColor2"}):
##        print r.find('a').text
##
