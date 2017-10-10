'''while True:
	# 0 is not prime
	# 1 is prime
	# numbers >1 are prime if only number%1==0 or number%number==0 
	result = 1 # 0 for not prime, 1 for prime
	number = int(input('Please enter a number: '))
	if number<=0: result = 0
	elif number>=1 and number<=3: result = 1
	else:
		for i in range(2,number):
			print(i) # temp 
			if number%i==0:
				result = 0
			print(result)# temp
	if result==0: print('Your number is not prime')
	else: print('Your number is prime')
	b = input('Exit? (Y)')
	if b=='Y': break'''

def getInt(phrase='Please specify a number: '):
	return(int(input(phrase)))

def isPrime(number):
	divisors = [x for x in range(2,number) if number%x==0]
	if number<=0: return False
	elif (number>=1 and number<=3) or divisors == []: return True

while True:
	if isPrime(getInt('Number? ')):
		print('Yep, your number is prime')
	else:
		print('Nope, your number isn\'n prime')
	b = input('Another try? (N to exit)')
	if b=='N': break
