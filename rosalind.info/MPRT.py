# Finding a Protein Motif 
# http://rosalind.info/problems/mprt/
import requests
from bs4 import BeautifulSoup

# 1. Import task data
with open('rosalind_mprt.txt','r') as f:
	fasta_ids = [x.strip() for x in f.readlines()]

# 2. Make urls for further data gathering
uniprot_urls = []
for i in range(len(fasta_ids)):
	url = 'http://www.uniprot.org/uniprot/'+fasta_ids[i]+'.fasta'
	uniprot_urls.append(url)

# 3. Function that takes an url, gets fasta-format protein sequence
# from uniprot.org, parses it for protein sequence, searches 
# N-glycosylation motif in protein sequens (N{P}[ST]{P}, where {P} -
# any aminoacid except P, [ST] S or T. If no such motif, returns False,
# else returns protein ID + positions of motif
def search4Nglycomotif(url):
	r = requests.get(url)
	r_html = r.text
	soup = BeautifulSoup(r_html,'html.parser')
	# get all info from Uniprot page
	uniprot_text = soup.get_text()
	# take only protein sequence
	temp_list = uniprot_text.split('\n')
	ps = ''
	for i in range(1,len(temp_list)):
		ps+=temp_list[i]
	# look for 4-character pieces N-not_P-S_or_T-not_P
	positions = []
	for i in range(1,len(ps)-3):
		if ps[i]=='N' and ps[i+1]!='P' and (ps[i+2]=='S' or ps[i+2]=='T') and ps[i+3]!='P':
			positions.append(i+1)
	if len(positions)==0:
		return False
	else:
		return(positions)

# 4. Iterate througn our proteins ID list (uniprot_urls) and 
# get the final results using function search4Nglycomotif
for i in range(len(uniprot_urls)):
	positions = []
	positions = search4Nglycomotif(uniprot_urls[i])
	if positions:
		print(fasta_ids[i])
		output = ''
		for x in range(len(positions)):
			output+=str(positions[x])+' '
		print(output.strip())
