import random

a = random.randint(1,9)
i = 0

while True:
	b = int(input('Please specify a number from 1 to 9 (inclusive): '))
	while b<1 or b>9:
		b = int(input('Please specify a number from 1 to 9 (inclusive): '))

	i += 1
	if b<a:
		print('Too low!')
	elif b==a:
		print('Exactly!')
		print('You tried',i,' times.')
		break
	else:
		print('Too high!')

	d = input('Try again? (Y/N)')
	if d=='N':
		break

print(a)