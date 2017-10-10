### 1
'''
a = 998
b = 944
c = a**2 + b**2
print(c)

### 2
s = 'NfwR7g1q5sWofq8FhBombyxobVXhesYbXps8ijofbH1PuXdceo5breP7r7Htk0cg3ZfM3Am3sBnbLf16ik3JsdkK6Jph8BftOFilQ9Eyed1ZguUcdispar7xRYRwYtlNJF1MClt8fgESteDuCwI6QgLq8kuAZ1q'
a = 17
b = 22
c = 112
d = 117
result = s[a:(b+1)] + ' ' + s[c:(d+1)] 
print(result)

### 3
a = 4199
b = 8434
sum = 0
for i in range(a,b+1):
	if i%2!=0:
		sum+=i
print(sum)


### 4
mytext = []
with open('rosalind_ini5.txt','r') as open_file:
	line = open_file.readline()
	line.strip()
	while line:
		mytext.append(line)
		line = open_file.readline()
print(mytext)
with open('result.txt','w') as file2write:
	for i in range(len(mytext)):
		if i%2==1:
			file2write.write(mytext[i])
print('ready')

### 4b
mytext = []
with open('rosalind_ini5.txt','r') as open_file:
	with open('result.txt','w') as file2write:
		file2write.write(''.join(open_file.readlines()[1::2]))

### 5
with open('rosalind_ini6.txt','r') as openfile:
	mylist = openfile.readlines()
	mystring = str(mylist[0])
	listfrommystring = mystring.split()

mydict = {}

for i in listfrommystring:
	if i in mydict:
		mydict[i]+=1
	else:
		mydict[i]=1

for key, value in mydict.items():
	print(key,value)

### 6





