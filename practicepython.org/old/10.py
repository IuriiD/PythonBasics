a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#import random

#while True:
	#a = random.sample(range(1,100),10)
	#b = random.sample(range(1,100),20)
c = [x for x in set(a) if x in b]
print(a)
print(b)
print(c)

	#d = input('Try again? (Y/N) ')
	#if d=='N':
	#	break