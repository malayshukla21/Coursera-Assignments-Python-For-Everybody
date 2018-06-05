fname = input("Enter the name of file: ")
try : 
	handle = open(fname)
except :
	print("Cannot open the file ",fname)

hour = dict()
for line in handle:
	if not line.startswith('From ') : 
		continue
	words = line.split()
	time = words[5]
	time = time.split(':')
	hour[time[0]] = hour.get(time[0],0) + 1 

tmp = list()
for key,value in hour.items() :
	tup = (key,value)
	tmp.append(tup)

tmp = sorted(tmp)

for key,value in tmp:
	print(key,value)

