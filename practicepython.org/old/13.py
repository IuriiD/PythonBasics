def howmuch():
	b = int(input('Please specify a number: '))
	while b<1:
		b = int(input('Please specify a number: '))
	return b

def fibogenerator(b):
	fiborange = []
	for x in range(b):
		if x == 0: fiborange.append(1)
		elif x == 1: fiborange.append(1+0)
		else: fiborange.append(fiborange[x-1]+fiborange[x-2])
	print(fiborange)

while True:
	fibogenerator(howmuch())
	if input('Exit (Y)? ')=='Y': break