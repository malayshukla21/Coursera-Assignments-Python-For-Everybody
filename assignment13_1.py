import urllib.request , urllib.parse , urllib.error
url = input("Enter location:")
xmlfile = urllib.request.urlopen(url).read()

import xml.etree.ElementTree as ET 
tree = ET.fromstring(xmlfile)
countTagList = tree.findall('comments/comment')

print('Retrieving',url)
print('Retrieved' , len(xmlfile) ,'characters')
print('Count:',len(countTagList))

counter = list()

for countTag in countTagList :
	count = countTag.find('count').text
	counter.append(count)


for i in range(0,len(counter)) :
	counter[i] = int(counter[i])

print('Sum:',sum(counter))