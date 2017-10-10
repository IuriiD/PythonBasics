# Transcribing DNA into RNA
# http://rosalind.info/problems/rna/

with open('rosalind_rna.txt','r') as openfile:
	line = openfile.readline().strip()

print(line.replace('T','U'))
