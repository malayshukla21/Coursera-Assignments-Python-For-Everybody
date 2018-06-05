import urllib.request , urllib.parse , urllib.error
import json

url = input('Enter location: ')
print('Retrieving',url)
urlHandle = urllib.request.urlopen(url)
data = urlHandle.read().decode()
print('Retrieved',len(data),'characters')
js = json.loads(data)

#print('Retrieved', len(js['comments']) ,'characters' )

length = len(js['comments'])

print('Count',length)

counts = list()

for numbers in range(0,length) :
	counts.append(js['comments'][numbers]['count'])
print('Sum:',sum(counts))