import urllib2
from urllib2 import Request
from bs4 import BeautifulSoup


#A small tutorial to learn beautifulsoup to scap tweets from any user based
# on profile link

theurl = Request("https://twitter.com/rishikeshkush")
thepage = urllib2.urlopen(theurl)
soup = BeautifulSoup(thepage,"html.parser")

print(soup.title)
#print soup.title.text
#print(soup.findAll('a'))

"""
for link in soup.findAll('a'):
    print link.get('href')
    print link.text
"""

print soup.findAll('a')[0]
#if soup.find('div',{"class":"ProfileHeaderClass"}).find('p') is not None:
print soup.find('div', {"class":"ProfileHeaderCard"}).find('p').text

i=1
print soup.title.text
for tweets in soup.findAll('div', {"class":"js-tweet-text-container"}):
    print i,": ",tweets.find('p').text
    i=i+1
