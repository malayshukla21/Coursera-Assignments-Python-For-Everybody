hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter the rate per Hour:")
rate = float(rate)
if hrs <= 40 :
	gross = hrs*rate
else :
	extra = hrs - 40
	gross = 40*rate + 1.5*extra*rate
print(gross)