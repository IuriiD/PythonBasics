def RecursiveSum(myint):
	while myint>9:
		input_list = [int(i) for i in str(myint)]
		mysum_int = sum(input_list)
	return mysum_int

print(RecursiveSum(56))
