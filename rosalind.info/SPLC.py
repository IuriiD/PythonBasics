# RNA Splicing
# http://rosalind.info/problems/splc/

# 1. Import task
temp_key = ''
inputdatadic = {}
inputdata = []
with open('rosalind_splc.txt','r') as f:
	line = f.readline().strip()
	while line:
		if line[:1]=='>':
			temp_key = line[1:]
		else:
			if temp_key not in inputdatadic.keys():
				inputdatadic[temp_key] = ''
			inputdatadic[temp_key]+=line
		line = f.readline().strip()

for k,v in inputdatadic.items():
	inputdata.append(inputdatadic[k])
#print(inputdata)

# 2. Import DNA codon table
dna_list = []
dna_dict = {}
with open('dna.txt','r') as openfile:
	line = openfile.readline().strip()
	while line:
		dna_list = line.split()
		for i in range(0,7,2):
			dna_dict[dna_list[i]]=dna_list[i+1]
		line = openfile.readline().strip()

# 3. Now remove introns
spliced = inputdata[0]
for i in range(1,len(inputdata)):
	spliced = spliced.replace(inputdata[i],'')

# 4.  function for DNA >> protein translation
def translatedna(inputdna):
	codons = []
	codons = [inputdna[i:i+3] for i in range(0, len(inputdna), 3)]
	protein = ''
	for i in codons:
		if i=='TAA' or i=='TAG' or i=='TGA' or len(i)<3:
			break
		else:
			#print(dna_dict[i])
			protein+=dna_dict[i]
	return(protein)

# 5. Result
print(translatedna(spliced))
