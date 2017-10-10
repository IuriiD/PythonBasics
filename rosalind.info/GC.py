# Computing GC Content
# http://rosalind.info/problems/gc/

def cdpercent(mystring):
	strlen = len(mystring)
	cg = mystring.count('C')+mystring.count('G')
	percent = round(cg*100/strlen,6)
	return percent

totalstr = ''
with open('rosalind_gc.txt','r') as openfile:
	line = openfile.readline()
	while line:
		totalstr+=line.strip()
		line = openfile.readline()

inputlist = []
inputlist = totalstr.split('>')

inputdic = {}
for i in range(1,len(inputlist)):
	inputdic[inputlist[i][0:13]]=inputlist[i][13:]

resultdic = {}
for key,value in inputdic.items():
	resultdic[key]=cdpercent(inputdic[key])

v=list(resultdic.values())
k=list(resultdic.keys())

print(k[v.index(max(v))])
print(max(v))