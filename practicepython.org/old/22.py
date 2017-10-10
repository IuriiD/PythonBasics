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

categoriesN = {}

with open('Training_01.txt','r') as open_file:
	line = open_file.readline()
	while line:
		line = line.strip()
		category = line[3:-26]
#		splittedl = line.split('/')
		if category in categoriesN:
			categoriesN[category]+=1
		else:
			categoriesN[category]=1
		line = open_file.readline()

for key, value in categoriesN.items():
	print(key,':',value)
