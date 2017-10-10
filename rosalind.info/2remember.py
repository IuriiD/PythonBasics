# 1
A, T, C, G = 0, 0, 0, 0
# print(A)

# 2
with open('rosalind_dna.txt','r') as open_file:
	line = open_file.readline()

# 2a
with open('rosalind_iprb.txt', 'r') as infile:
    (k, m, n) = (int(value) for value in infile.readline().split())

# 3
result = line.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[::-1]

# 4 
percent = round(cg*100/strlen,6)

#5 
with open('file.txt','r') as f:
	strands = [x.strip() for x in f.readlines()]

#6 - parces multiline FASTA-format input into a dictionary
temp_key = ''
inputdata = {}
with open('rosalind_gc.txt','r') as f:
	line = f.readline().strip()
	while line:
		if line[:1]=='>':
			temp_key = line[1:]
		else:
			if temp_key not in inputdata.keys():
				inputdata[temp_key] = ''
			inputdata[temp_key]+=line
		line = f.readline().strip()