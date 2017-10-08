import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

q = []
for x in range(1, random.randint(1,51)):
	q.append(random.randint(0, 100))

z = []
for x in range(1, random.randint(1,51)):
	z.append(random.randint(0, 100))

print(q, '\n')
print(z, '\n')
print([x for x in q if x in z])