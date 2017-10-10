def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
	output = []
	for number in range(a,b+1):
		inputlist = [int(x) for x in str(number)]
		mysum = 0
		for x in range(len(inputlist)):
			mysum += inputlist[x]**(x+1)
		if mysum==number:
			output.append(number)
	return output

print(sum_dig_pow(1,100))
