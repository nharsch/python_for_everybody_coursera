from sys import argv
import urllib
import BeautifulSoup as bs

script, url = argv

if 'http' not in url:
    url = 'http://{}'.format(url)

# url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = bs.BeautifulSoup(html)

# Retrieve a list of the anchor tags
# Each tag is like a dictionary 

tags = soup('a')

for tag in tags:
    print tag.get('href', None)
