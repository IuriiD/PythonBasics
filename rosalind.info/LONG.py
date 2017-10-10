# Genome Assembly as Shortest Superstring
# http://rosalind.info/problems/long/

# 1. Import task
temp_key = ''
inputdata = {}
with open('file.txt','r') as f:
	line = f.readline().strip()
	while line:
		if line[:1]=='>':
			temp_key = line[1:]
		else:
			if temp_key not in inputdata.keys():
				inputdata[temp_key] = ''
			inputdata[temp_key]+=line
		line = f.readline().strip()

print(inputdata)