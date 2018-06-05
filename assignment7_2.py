fname = input("Enter the filename: ")
try :
	fhandle = open(fname)
except :
	print('Cannot open the file ',fname)

val_count = 0
line_count = 0
avg = 0

for line in fhandle:
	if not line.startswith("X-DSPAM-Confidence:") :
		continue

	line_count = line_count + 1
	iPos = line.find('0')
	value = line[iPos:]
	value = float(value)
	val_count = val_count + value



avg = val_count/line_count
print('Average spam confidence:', avg)