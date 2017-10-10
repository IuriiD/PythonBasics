import random

number = random.randint(1000,9999)
print(number)
print('Welcome to Cows and Bulls game!')


def cowsNbullsN(number,guess):
	list_number = list(str(number))
	list_guess = list(str(guess))
	cowsN = 0
	bullsN = 0
	for i in range(4):
		if list_number[i] in list_guess:
			if list_number[i]==list_guess[i]:
				cowsN+=1
			else:
				bullsN+=1
	if list_number==list_guess:
		print('You won!')
		return(False)
	else:
		print(cowsN,'cows, ',bullsN,'bulls')
		return(True)

while True:
	guess = input('Please, enter a number (0..9999): ')
	if not cowsNbullsN(number,guess):
		break