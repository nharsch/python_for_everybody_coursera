import urllib
import BeautifulSoup as bs

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = bs.BeautifulSoup(html)

# Retrieve a list of the anchor tags
# Each tag is like a dictionary 

tags = soup('a')

for tag in tags:
    print tag.get('href', None)
