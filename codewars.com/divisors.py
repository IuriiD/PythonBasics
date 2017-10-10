def divisors(intnum):
	result = []
	for n in range(2,intnum):
		if intnum%n==0:
			result.append(n)
	if result==[]:
		return (str(intnum)+' is prime')
	else:
		return result

print(divisors(13))

#result = [a for a in range(2,intnum) if intnum%a==0]