# Complementing a Strand of DNA
# http://rosalind.info/problems/revc/

### 3
with open('rosalind_revc.txt','r') as openfile:
	line = openfile.readline().strip()

result = ''
linereversed = line[::-1]
for i in linereversed:
	if i=='A': result+='T'
	elif i=='T': result+='A'
	elif i=='C': result+='G'
	elif i=='G': result+='C'
print('input: ',line)
print('***')
print('reversed: ',linereversed)
print('***')
print('result: ',result)


### Alternatively 

'''with open('rosalind_revc.txt','r') as openfile:
	line = openfile.readline().strip()

result = line.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[::-1]
print(line)
print('***')
print(result)'''