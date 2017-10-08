number = int(input('Please define a number: '))

'''divisors = []

for x in range(1, number):
	if number % x == 0:
		divisors.append(x)
print(divisors)'''

print([x for x in range(1,number) if number % x == 0])
