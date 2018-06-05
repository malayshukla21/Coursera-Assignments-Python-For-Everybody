fhandle = open('mbox-short.txt')
val_count = 0
line_count = 0
avg = 0
for line in fhandle:
	if not line.startswith("X-DSPAM-Confidence:") :
		continue
	print(line)
	line_count = line_count + 1
	iPos = line.find('0')
	value = line[iPos:]
	value = float(value)
	val_count = val_count + value



print(line_count)
print(val_count)
avg = val_count/line_count
print(avg)