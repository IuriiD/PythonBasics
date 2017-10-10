# let's create a dictionary {'Name': count}
'''namescount = {}

with open('nameslist.txt','r') as open_file:
	line = open_file.readline()
	while line:
		line = line.strip()
		# check if this key is in dictionary
		if line in namescount:
		# if it is, corresp. value+=1
			namescount[line]+=1
		# if it doesn't exist, add such a key to dictionary and value = 1
		else:
			namescount[line]=1
		line = open_file.readline()

print(namescount)'''

### another varian
'''primenumberslist = []
happynumberslist = []

with open('primenumbers.txt','r') as primes:
	line = primes.readline()
	while line:
		line = line.strip()
		primenumberslist.append(line)
		line = primes.readline()

with open('happynumbers.txt','r') as happies:
	line = happies.readline()
	while line:
		line = line.strip()
		happynumberslist.append(line)
		line = happies.readline()

overlapping = []
overlapping = [i for i in primenumberslist if i in happynumberslist]
print(overlapping)'''

###### again with functions
def filetolist(filename):
	output = []
	with open(filename,'r') as open_file:
		line = open_file.readline()
		while line:
			line = line.strip()
			output.append(line)
			line = open_file.readline()
	return output

primenumberslist = filetolist('primenumbers.txt')
happynumberslist = filetolist('happynumbers.txt')

overlapping = []
overlapping = [i for i in primenumberslist if i in happynumberslist]
print(overlapping)