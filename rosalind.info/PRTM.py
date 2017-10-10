# Locating Restriction Sites
# http://rosalind.info/problems/revp/

# 1. Import task
sequence = ''
with open('rosalind_revp.txt','r') as f:
	line = f.readline().strip()
	while line:
		if line[:1]!='>':
			sequence+=line
		line = f.readline().strip()
print(sequence,len(sequence))

# 2. Let's search for reverse palindromes length 4-12
results = {}

# v1 

for i in range(4,13,2):
	for n in range(len(sequence)-i+1):
		left = sequence[n:n+i//2]
		right = sequence[(n+i//2):(n+i)]
		right_inversed = right[::-1]
		right_complement = right_inversed.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
		#print(i,n,left,right,'(',right_complement,')')
		if left==right_complement:
			results[n+1]=i

# v2 - can't understand why it doesn't work
'''
for i in range(4,13,2):
	for n in range(len(sequence)-i+1):
		direct = sequence[n:n+i]
		rev = direct[::-1]
		rev_compl = rev.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
		print(n+1,direct,rev,rev_compl)
	if direct==rev_compl:
		print('!')
		results[n+1]=i
'''

for k,v in results.items():
	print(k,v)
