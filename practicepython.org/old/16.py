'''from random import randint

def randomletter():
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	x = randint(0,25)
	return alphabet[x]

def randomnumber():
	return randint(1,9)

def randomsign():
	alphabet = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/'] # 14
	b = randint(0,12)
	return alphabet[b]

def upperlower(letter):
	z = randint(1,2)
	if z==1:
		letter=letter.lower()
	else:
		letter=letter.upper()
	return letter

while True:
	length = int(input('How long should it be? '))
	pwd = []
	for i in range(length):
		y = randint(1,3) # letter (1), number (2) or symbol (3)?
		if y==1:
			pwd.append(upperlower(randomletter()))
		elif y==2:
			pwd.append(str(randomnumber()))
		else:
			pwd.append(randomsign())
		
	result = ''.join(pwd)
	print(result)

	if input('Exit (Y)? ')=='Y': break'''

import random
while True:
	alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
	password = ''
	length = int(input('How long should it be? '))
	password = ''.join(random.sample(alphabet,length))
	print(password)
	if input('Exit (Y)? ')=='Y': break