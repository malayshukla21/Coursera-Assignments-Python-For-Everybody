import re
handle = open('actualdata.txt')
file = handle.read()
num = re.findall('[0-9]+',file)

for i in range(0,len(num)) :
	num[i] = int(num[i])

sumnum = sum(num)
print(sumnum)