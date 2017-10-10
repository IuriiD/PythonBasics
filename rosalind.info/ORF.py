# Open Reading Frames
# http://rosalind.info/problems/orf/

dna_list = []
dna_dict = {}
temp_key = ''
inputdata = ''


# 1. Import DNA codon table (http://rosalind.info/glossary/dna-codon-table/)
# ATG - DNA start-codon (AUG for RNA)
with open('dna.txt','r') as openfile:
	line = openfile.readline().strip()
	while line:
		dna_list = line.split()
		for i in range(0,7,2):
			dna_dict[dna_list[i]]=dna_list[i+1]
		line = openfile.readline().strip()

# 2. Import DNA sequence
with open('rosalind_orf.txt','r') as f:
	line = f.readline().strip()
	while line:
		if line[:1]!='>':
			inputdata+=line
		line = f.readline().strip()

print(inputdata,'\n')

# 3. Complementary DNA string
inversed = inputdata.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[::-1]
#print(inversed)

# 4. Search for open reading frames (ORF)
def look4ORF(dnasequence):
	proteinlist = []
	flagup = False
	protein = ''
	codon = ''
	additionalATG = []

	for i in range(0,len(dnasequence),3):
		codon = dnasequence[i:i+3]
		if codon=='ATG':
			protein+='M'
			if flagup==False:
				flagup=True
			else:
				# for the case when 'inside' of the bigger protein sequence
				# there's another, smaller protein - let's store positions
				# of such 'M' residues in 'protein' and then if ORF is
				# confirmed (stop-codon found) then we flush the original
				# protein to 'proteinlist' and also those 'inside' ones
				additionalATG.append(len(protein))
		elif codon=='TAA' or codon=='TAG' or codon=='TGA' and flagup==True:
			flagup=False
			if protein!='' and protein not in proteinlist:
				#print(protein)
				proteinlist.append(protein)
				if additionalATG!=[]:
					for x in additionalATG:
						if protein[x-1:] not in proteinlist:
							#print(protein[x-1:])
							proteinlist.append(protein[x-1:])
			protein=''
			additionalATG = []
		else:
			if flagup==True and len(codon)==3:
				protein+=dna_dict[codon]
	#print(proteinlist)
	return proteinlist

# 5. Final search for proteins
finalresults = []
for n in range(3):
	finalresults.append(look4ORF(inputdata[n:]))
	finalresults.append(look4ORF(inversed[n:]))

#print(finalresults)

finalfinal = []
for sublist in finalresults:
	if sublist!='':
		if type(sublist)==list:
			for i in sublist:
				finalfinal.append(i)

finalfinal=set(finalfinal)
for i in finalfinal:
	print(i)