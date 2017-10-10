# Enumerating Gene Orders
# http://rosalind.info/problems/perm/
import random

# 1. Import task
with open('rosalind_perm.txt','r') as f:
	n = int(f.readline().strip())
print('n=',n)

# 2. Let's calculate the number of possible permutations
perm_qnt = 1

for i in range(n):
	perm_qnt*=(n-i)

# 3. Le'ts generate possible variants of permutations
def randcomb(n):
	variants = [0]*n
	for i in range(n):
		while variants[i]==0:
			y = random.randint(1,n)
			if y not in variants:
				variants[i]=y
	#print(variants)
	return(variants)

all_perm = []
while len(all_perm)!=perm_qnt:
	temp = randcomb(n)
	if temp not in all_perm:
		all_perm.append(temp)

print(len(all_perm))
for i in all_perm:
	line = ''
	for x in i:
		line+=str(x)+' '
	print(line)
