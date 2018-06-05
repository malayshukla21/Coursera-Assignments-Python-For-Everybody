fname = input("Enter the file name: ")
try :
	fhandle = open(fname)
except :
	print ('Cannot open the file.')
	quit()

words = list()

for line in fhandle :
	line = line.rstrip()
	words = line.split() + words 

words = sorted(words)

wordFinal = list()
for word in words :
	if word not in wordFinal :
		wordFinal.append(word)

print(wordFinal)
