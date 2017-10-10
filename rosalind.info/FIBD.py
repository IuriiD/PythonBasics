#Mortal Fibonacci Rabbits
# http://rosalind.info/problems/fibd/

n = 0 # duration of experiment, months
m = 0 # rabbit's live duration, months
inputlist = []
with open('file.txt','r') as open_file:
	inputlist = open_file.readline().strip().split(' ')
	n = int(inputlist[0]) 
	m = int(inputlist[1]) 

rabbits = [0]*m
temp_rabbits = [0]*m

for i in range(n):
	if i==0:
		rabbits[0]=1
	else:
		temp_rabbits = [0]*m
		temp_rabbits[0]=sum(rabbits[1:])
		for x in range(1,m):
			temp_rabbits[x]=rabbits[x-1]
		rabbits=temp_rabbits
print(sum(rabbits))