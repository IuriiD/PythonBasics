# Mendel's First Law
# http://rosalind.info/problems/iprb/

# k - AA
# m - Aa
# n - aa
# AA or Aa
with open('rosalind_iprb.txt','r') as openfile:
	line = openfile.readline().strip()
	mylist = line.split()
print(line)
print(mylist)
k = int(mylist[0])
m = int(mylist[1])
n = int(mylist[2])

print(k, m, n)

sum = k+m+n
#m*m*0.75+m*n*0.5
#aa = 0

mm0_25 = m/sum * (m-1)/(sum-1) * 1/4

mn1_2 = m/sum * n/(sum-1) * 1#/2

nn1 = n/sum * (n-1)/(sum-1) * 1

print('mm0_25=',mm0_25)
print('mn1_2=',mn1_2)
print('nn1=',nn1)
aa = mm0_25 + mn1_2 + nn1
print('aa=',aa)
Ax = 1-aa
print('Ax=',Ax)