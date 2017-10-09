phrase = input('Please enter some phrase: ')

if phrase == phrase[::-1]:
	print('Hey, that\'s a palindrome!')
else:
	print('No, that\'s not a palindrome')
