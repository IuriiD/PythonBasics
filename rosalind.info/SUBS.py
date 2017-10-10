# Finding a Motif in DNA
# http://rosalind.info/problems/subs/

with open('rosalind_subs.txt','r') as openfile:
	s,t = openfile.read().split()
poslist = []
ls = len(s)
lt = len(t)


for i in range(ls):
	#print('s[i:i+lt]=',s[i:i+lt])
	if s[i:i+lt]==t:
		poslist.append(i+1)

resultstr = ''
for i in poslist:
	resultstr+=str(i)+' '

print(resultstr)