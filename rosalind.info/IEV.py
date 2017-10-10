# Calculating Expected Offspring
# http://rosalind.info/problems/iev/

'''
AA-AA - r1 - 100% A_
AA-Aa - r2 - 100% A_
AA-aa - r3 - 100% A_
Aa-Aa - r4 - 75% A_, 25% aa
Aa-aa - r5 - 50% A_, 50% aa
aa-aa - r6 - 0% A_, 100% aa
Let's calculate the probability of getting aa offsprings and
totalN-double.recessive
'''

# 1. Import input
with open('rosalind_iev.txt','r') as f:
	r1, r2, r3, r4, r5, r6 = [int(i) for i in f.read().split()]
	
# 2. Calculate how much aa offsprings we'll get (r4 gives 25%, r5 - 50%, r6 - 100%,
# each pair gives 2 offsprings)
aa = r4*0.25*2 + r5*0.5*2 + r6*2

# 3. Total number of offsprings
total = (r1 + r2 + r3 + r4 + r5 + r6)*2

# 4. A_ offsprings
result = total - aa

print(result)
