words = []
with open('text.txt', 'r') as f:
	for line in f:
		words.extend(line.split())

lengths = [] 
for x in words:
	lengths.append(len(x))

average = sum(lengths) / len(lengths)

print(words)
print
print(lengths)
print
print(average)
