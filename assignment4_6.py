def computepay(h,r) :
	if hrs <= 40 :
		gross = h*r
	else :
		extra = h - 40
		gross = 40*r + 1.5*extra*r
	return gross


hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter the rate per Hour:")
rate = float(rate)
pay = computepay(hrs,rate)
print(pay)
