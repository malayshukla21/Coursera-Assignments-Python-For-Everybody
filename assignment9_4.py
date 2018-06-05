name = input('Enter the name :')
handle = open(name)

counts = dict()

for line in handle :
	line.rstrip()
	if not line.startswith('From ') :
		continue
	words = line.split()
	counts[words[1]] = counts.get(words[1],0) + 1

bigcount = None
bigname = None

for keys,values in counts.items() : 
	if bigcount is None or values > bigcount :
		bigcount = values
		bigname = keys

print(bigname,bigcount)