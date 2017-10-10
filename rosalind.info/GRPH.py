# Overlap Graphs
# http://rosalind.info/problems/grph/

# variables
tempstr = '' # import and parcing of input data
templist = [] # import and parcing of input data

fastakeys = [] # a list of names for strings in Fasta format (like 'Rosalind_0498')
fastastrings = [] # a list for strings (like 'GGGTGGG')

pair = '' # auxiliary variable
resultlist = [] # final results (pairs of string keys in Fasta format)

# import to string
with open('rosalind_grph.txt','r') as openfile:
	line = openfile.readline().strip()
	while line:
		tempstr+=line
		line = openfile.readline().strip()

# string to list
templist = tempstr.split('>')

# list to dictionary
for i in range(1,len(templist)):
	fastakeys.append(templist[i][:13])
	fastastrings.append(templist[i][13:])

cycles = len(fastakeys)
for i in range(cycles):
	for x in range(cycles):
		if fastastrings[i]!=fastastrings[x] and fastastrings[i][-3:]==fastastrings[x][:3]:
			pair = fastakeys[i]+' '+fastakeys[x]
			if pair not in resultlist:
				resultlist.append(pair)

for value in resultlist:
	print(value)