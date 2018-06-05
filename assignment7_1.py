fname = input("Enter the name of the file: ")
try :
	fhandle = open(fname)
except : 
	print('File cannot be opened')
	quit()

fullFile = fhandle.read()
fullFile = fullFile.upper()
fullFile = fullFile.rstrip()
print(fullFile)
