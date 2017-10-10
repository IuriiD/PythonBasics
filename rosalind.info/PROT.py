# Translating RNA into Protein
# http://rosalind.info/problems/prot/

rna_list = []
rna_dict = {}
input_rna = ''

# import RNA codon table
with open('rna.txt','r') as openfile:
	line = openfile.readline().strip()
	while line:
		rna_list = line.split()
		for i in range(0,7,2):
			rna_dict[rna_list[i]]=rna_list[i+1]
		line = openfile.readline().strip()

# import RNA
with open('rosalind_prot.txt','r') as openfile:
	line = openfile.readline().strip()
	while line:
		input_rna+=line
		line = openfile.readline().strip()

# split RNA into codons
codons = []
codons = [input_rna[i:i+3] for i in range(0, len(input_rna), 3)]

# translate RNA into protein
aaresult = ''
for i in codons:
	if i=='UAA' or i=='UAG' or i=='UGA':
		break
	else:
		aaresult+=rna_dict.get(i)

# print result
print(aaresult)