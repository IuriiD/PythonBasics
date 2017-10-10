from random import randint
a = [randint(1,100) for i in range(10)]
b = [randint(1,100) for i in range(20)]
c = []
# c = [x for x in a if x in b]
'''for i in range(len(a)):
	for x in range(len(b)):
		if a[i]==b[x]:
			if a[i] not in c:
				c.append(a[i])'''

'''for i in range(len(a)):
	if a[i] in b:
		if a[i] not in c:
			c.append(a[i])'''

'''for i in a:
	if i in b and i not in c:
		c.append(i)'''

c = [x for x in set(a) if x in b]
print(a, '\n', b, '\n', c)
