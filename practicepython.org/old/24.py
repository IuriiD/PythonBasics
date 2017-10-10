rows = int(input('How many rows (>1)? '))
while rows<=1:
	rows = int(input('How many rows (>1)? '))

columns = int(input('How many colymns (>1)? '))
while columns<=1:
	columns = int(input('How many colymns (>1)? '))

delimiter = ' ---'*columns
lines = '|'+'   |'*columns

for i in range(0,rows):
	print(delimiter)
	print(lines)
print(delimiter)
