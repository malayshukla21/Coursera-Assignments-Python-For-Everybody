fn = input('Enter the name of file :')
try :
	fh = open(fn)
except : 
	print('Cannot open the requested file.')
	quit()

emails = list()
count = 0 

for line in fh :
	line = line.rstrip()
	if not line.startswith('From ') : 
		continue
	words = line.split()
	emails.append(words[1])
	count = count + 1

for email in emails :
	print(email)

print('There were',count,'lines in the file with From as the first word')