# Inferring mRNA from Protein
# http://rosalind.info/problems/mrna/

rna_list = []
rna_dict = {}
protseq = ''
codonvariants = {}
rnavariants = 1

# 1. Import RNA codon table (http://rosalind.info/glossary/rna-codon-table/)
with open('rna.txt','r') as openfile:
	line = openfile.readline().strip()
	while line:
		rna_list = line.split()
		for i in range(0,7,2):
			rna_dict[rna_list[i]]=rna_list[i+1]
		line = openfile.readline().strip()

# 2. Import protein sequence (task)
with open('rosalind_mrna.txt','r') as openfile:
	line = openfile.readline().strip()
	while line:
		protseq+=line
		line = openfile.readline().strip()

# 3. Create a dictionary - how many codons for each aminoacid (aa) (+ stop-codons)
for key,value in rna_dict.items():
	if value in codonvariants:
		codonvariants[value]+=1
	else:
		codonvariants[value]=1

# 4. Count for number of rna variants
for i in range(len(protseq)):
	rnavariants*=codonvariants[protseq[i]]
rnavariants*=codonvariants['Stop']
result = rnavariants % 1000000
print(result)