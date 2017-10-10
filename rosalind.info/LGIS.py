# Longest Increasing Subsequence
# http://rosalind.info/problems/lgis/

# 1. Import task
with open('file.txt','r') as f:
	n = f.readline().strip()
	perm = [int(i) for i in f.readline().strip().split(' ')]
print(perm)
# 2. Function for an increasing subsequence search (to find
# a decreasing - just input [::-1])
'''def longesttrendingsubs(mylist):
	result = []
	result.append(mylist[len(mylist)-1])

	for i in range(result[len(result)-1],0,-1):
		if i in mylist[:mylist.index(result[len(result)-1])]:
			result.append(i)
	return result

print('sequence=',perm)
print('inverted=',perm[::-1])
print('longest decreasing:',longesttrendingsubs(perm))
inverted = perm[::-1]
print('longest increasing:',longesttrendingsubs(inverted))
'''
