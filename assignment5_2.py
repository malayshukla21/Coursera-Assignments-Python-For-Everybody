#to find largest and smallest number
largest = -1
smallest = None
while True :
	try :
		num = input("Enter a number:")
		#to stop the loop when input is done
		if num == 'done' :
			break

		num = int(num)
		
		#to find the largest number
		if largest < num : 
			largest = num

		#to find the smallest number
		if smallest is None :
			smallest = num
		elif smallest > num :
			smallest = num 

	except :
		print("Invalid input")

print('Maximum is',largest)
print('Minimum is',smallest)

