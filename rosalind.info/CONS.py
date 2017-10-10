# Consensus and Profile
# http://rosalind.info/problems/cons/

strdict = {}
bigstring = ''
biglist = []
with open('rosalind_cons.txt','r') as f:
	line = f.readline()
	while line:
		bigstring+=line.strip()
		line = f.readline()
biglist = bigstring.split('>')
#print(biglist)

n = 13
strdict = {biglist[i][0:n]: biglist[i][n:] for i in range(1, len(biglist))}
#print(strdict)

strlen = len(strdict[next(iter(strdict))])
countA = [0]*strlen
countC = [0]*strlen
countG = [0]*strlen
countT = [0]*strlen

for i in range(strlen):
	for value in strdict.values():
		#print('i=',i,'; value=',value,'; value[i]=',value[i])
		if value[i]=='A':
			countA[i]+=1
		elif value[i]=='C':
			countC[i]+=1
		elif value[i]=='G':
			countG[i]+=1
		elif value[i]=='T':
			countT[i]+=1

consensus = ''
maxval = 0
for i in range(strlen):
	maxval = max(countA[i],countC[i],countG[i],countT[i])
	if countA[i]==maxval:
		consensus+='A'
	elif countC[i]==maxval:
		consensus+='C'
	elif countG[i]==maxval:
		consensus+='G'
	elif countT[i]==maxval:
		consensus+='T'
print(consensus)

strA = ''
strC = ''
strG = ''
strT = ''
for i in range(strlen):
	strA+=str(countA[i])+' '
	strC+=str(countC[i])+' '
	strG+=str(countG[i])+' '
	strT+=str(countT[i])+' '

print('A:',	strA)
print('C:',	strC)
print('G:',	strG)
print('T:',	strT)