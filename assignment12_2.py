import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup

import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter position: ')
count = int(count)
position = int(position)



html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

print('Retrieving:',url)

tags = soup('a')
links = list()

for tag in tags :
	links.append(tag.get('href',None))

linksPrime = links
linksPrime1 = list()

for counter in range(0,count) :
	htmlPrime = urllib.request.urlopen(linksPrime[position-1],context=ctx).read()
	soupPrime = BeautifulSoup(htmlPrime,'html.parser')
	print('Retrieving:',linksPrime[position-1])
	tagsPrime = soupPrime('a')

	for tagPrime in tagsPrime :
		linksPrime1.append(tagPrime.get('href',None))

	linksPrime = linksPrime1
	linksPrime1 = list()


