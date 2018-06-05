import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

numbers = list()
tags = soup('span')
for tag in tags :
	numbers.append(tag.contents[0])

for number in range(0,len(numbers)) :
	numbers[number] = int(numbers[number])

summation = sum(numbers)
print('Count',len(numbers))
print('Sum',summation)