# Counting Point Mutations
# http://rosalind.info/problems/hamm/

with open('rosalind_hamm.txt','r') as openfile:
	s = openfile.readline()
	t = openfile.readline()
hammdist = 0
print(s)
print(t)

for i in range(len(s)):
	if s[i]!=t[i]:
		hammdist+=1

print(hammdist)