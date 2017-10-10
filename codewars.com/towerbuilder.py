def tower_builder(n_floors):
	stars = []
	for n in range(1,n_floors+1):
		if n == 1: 
			x = 1
			stars.append('*')
		else: 
			x+=2
			stars.append('*'*x)
	
	if n_floors==1:
		return ['*',]
	else:
		result = []
		spaces = ''
		for y in range(n_floors):
			spaces = (x-len(stars[y]))//2*' '
			result.append(spaces+stars[y]+spaces)
		return(result)

print(tower_builder(6))
