# Enumerating k-mers Lexicographically
# http://rosalind.info/problems/lexf/
import itertools

# 1. Import task
with open('rosalind_lexf.txt','r') as f:
	voc = f.readline().strip().split()
	n = int(f.readline().strip())
print(voc, n)

# 2. Generate all possible n-length combinations of characters from voc
var = list(itertools.product(voc,repeat=n))
variants = []

for x in range(len(var)):
	temp = ''
	for y in range(len(var[x])):
		temp+=var[x][y]
	variants.append(temp)

variants=sorted(variants)

for i in variants:
	print(i)
