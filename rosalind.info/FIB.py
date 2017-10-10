# Rabbits and Recurrence Relations
# http://rosalind.info/problems/fib/

n = 0
k = 0
inputlist = []
with open('rosalind_fib.txt','r') as open_file:
	line = open_file.readline().strip()
	inputlist = line.split(' ')
	n = int(inputlist[0])
	k = int(inputlist[1])
print(inputlist)
print('n=',n)
print('k=',k)

series = [[0,1,0],[1,0,0]] # mature/young/total, 1st and 2nd months
mature = 0
young = 0
total = 0

for x in range(2,n):
	print('\nMonth',x+1)
	mature = series[x-1][0] + series[x-2][0]*k
	print('mature=',mature)
	young = series[x-1][0]*k
	print('young=',young)
	total = mature + young
	print('total=',total)
	series.append([mature,young,total])
print(series)
print(series[-1][-1])