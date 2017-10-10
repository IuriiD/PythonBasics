'''
Stop gninnipS My sdroW!
Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more letter 
words reversed (Just like the name of this Kata). Strings passed 
in will consist of only letters and spaces. Spaces will be 
included only when more than one word is present.
'''

def spinWords(inputstr):
	input = [i for i in inputstr.split()]
	for x in range(len(input)):
		if len(input[x])>=5:
			input[x]=input[x][::-1]
	result = ' '.join(input)
	return result

print(spinWords('Hey fellow warriors'))

def spinWords_best(inputstr):
	return ' '.join(x[::-1] if len(x)>=5 else x for x in inputstr.split())

print(spinWords_best('Hey fellow warriors'))