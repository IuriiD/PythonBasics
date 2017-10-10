# Finding a Shared Motif
# http://rosalind.info/problems/lcsm/

# 1. Import data
temp_key = ''
inputdata = {}

with open('rosalind_lcsm.txt','r') as f:
	line = f.readline().strip()
	while line:
		if line[:1]=='>':
			temp_key = line[1:]
		else:
			if temp_key not in inputdata.keys():
				inputdata[temp_key] = ''
			inputdata[temp_key]+=line
		line = f.readline().strip()

#2. Let's find key-value pair with the shortest value
shotest_key = ''
shortest_value = '0'*1001
for key, value in inputdata.items():
	if len(value)<len(shortest_value):
		shortest_value = value
		shotest_key = key
#print('shortest_value=',shortest_value)

#3. Now let's look for similar sequences starting from 2 signs 
# and up to shortest_value
longest_common = ''
for i in range(2,len(shortest_value)): # for indenting strings length (min - 2)
	for x in range(len(shortest_value)+1-i): # for shifting the search "window"
		#print('i=',i,'x=',x,'search for',shortest_value[x:(i+x)])
		#if all(v for v in inputdata.values() if shortest_value[x:(i+x)] in v):
		if all(shortest_value[x:(i+x)] in v for v in inputdata.values()):
			longest_common = shortest_value[x:(i+x)]

#for v in inputdata.values():
#	print(v)
print('\n',longest_common)
# take the smallest string and check if it's in other
	# if all strings are of same lenght = continue
# take 2 first signs [0:2] of string0 and search for them in other strings
	# if they are in all other strings, store and go to 3 signs
# if no take the next 2 signs (2:4) etc
# if no, take 2 signs with 1 shift (1:3) etc
# if we have 2-sign common, go for 3 first signs
# search for +1-signs line until there's no - then take the previous found