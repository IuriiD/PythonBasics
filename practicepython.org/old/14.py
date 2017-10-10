'''def randintlist(n=15):
	import random
	a = [random.randint(0,10) for i in range(n)]
	return a

def removeduplicates(somelist):
	newlist = []
	for i in range(len(somelist)):
		if somelist[i] not in newlist:
			newlist.append(somelist[i])
	print(newlist)

print (randintlist(10))
removeduplicates(randintlist(10))
'''

def randintlist(n=15):
	import random
	return [random.randint(0,100) for i in range(n)]

def deduplicate(somelist):
	return set(somelist)

print(deduplicate(randintlist(10)))