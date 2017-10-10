# Counting DNA Nucleotides
# http://rosalind.info/problems/dna/

with open('rosalind_dna.txt','r') as open_file:
	line = open_file.readline()
print(line)
A, C, G, T = 0, 0, 0, 0

for i in line:
	if i=='A': A+=1
	elif i=='C': C+=1
	elif i=='G': G+=1
	elif i=='T': T+=1
print(A,C,G,T)
